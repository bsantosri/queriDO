
DROP TABLE IF EXISTS content CASCADE;

CREATE TABLE content (
   id bigserial NOT NULL PRIMARY KEY,
   urn_do text NOT NULL, -- urn baseada nos dados de info. jurisdicao:escopo:  ex. "br;rj;rio.janeiro:gov-exe:2015-02-13:materia:12334"
   urn_lex text,         -- urn baseada nos dados de kx extraídos do content 
   content XML NOT NULL,
   info JSONB,    -- informações aficionais (ex. data e código da matéria no diário oficial)
   kx JSONB,      -- cache para agilizar buscas XPath
   updated timestamp NOT NULL DEFAULT now(), 
   UNIQUE(urn_do),
   UNIQUE(urn_lex)
);
-- ideal criar trigger before insert or update para formação do campo urn_do e dar erro se veio nao-null.

-- 
--  LIB FUNCOES GENÉRICAS JSONB
-- 

CREATE OR REPLACE FUNCTION countword(text[])
  -- 
  -- Transform an array of strings into a JSONb array of objects, counting words.
  --
RETURNS JSONb AS $func$
   SELECT jsonb_agg(j) 
   FROM (
      SELECT x, json_build_object(x, count(x)) as j
      FROM unnest($1) t(x)
      GROUP BY x
   ) t;
$func$ LANGUAGE sql IMMUTABLE;


CREATE OR REPLACE FUNCTION remove_nulls(JSONb) 
RETURNS JSONb AS $func$
   SELECT jsonb_object_agg(key,value)
   FROM jsonb_each($1)
   WHERE jsonb_typeof(value)!='null'
;
$func$ LANGUAGE sql IMMUTABLE;


CREATE OR REPLACE FUNCTION jsonb_object_keys_count(JSONb) 
RETURNS bigint AS $func$
   SELECT count(*) FROM jsonb_object_keys($1)
;
$func$ LANGUAGE sql IMMUTABLE;


-- 
--  VIEWS E FUNCOES ESPECÍFICAS DO PROJETO
-- 

CREATE OR REPLACE FUNCTION content_count(xml)
  -- 
  -- Standard "check and count" analysis of content table.
  --
RETURNS JSONb AS $func$

   SELECT remove_nulls(to_jsonb(t)) 
   FROM (SELECT 
    countword(xpath('//cite/@class',$1)::text[]) AS cite,
    countword(xpath('//mark/@class',$1)::text[]) AS mark,
    countword(xpath('//data/@class',$1)::text[]) AS data,
    countword(xpath('//time/@class',$1)::text[]) AS time			 
   ) t;
$func$ LANGUAGE sql IMMUTABLE;

DROP VIEW IF EXISTS vw_content_rich;
CREATE VIEW vw_content_rich AS
   SELECT * FROM (
       SELECT *, jsonb_object_keys_count(kx) AS kx_keys FROM content
   ) t  
   WHERE  kx_keys>1
;
