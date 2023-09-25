-- 1) Consulta simples usando somente o básico SELECT, FROM, WHERE
SELECT * FROM public.usuario WHERE email = 'marcos.gabriel@ossirian.com';

-- 2) Consulta usando LIKE
SELECT * FROM public.usuario WHERE email LIKE  '%@email.com';

-- 3) Consulta usando operadores de conjuntos
-- TODO: Esta meio errado, achar duas tabelas com atributos identicos
SELECT email, senha FROM public.usuario
UNION
SELECT primeiro_nome, sobrenome FROM public.pessoafisica;

-- 4) Consulta usando um JOIN
SELECT * FROM public.usuario u
    JOIN pessoafisica p ON u.id = p.usuario;

-- 5) Consulta usando mais de um JOIN
SELECT * FROM public.usuario u
    JOIN pessoafisica p ON u.id = p.usuario
    JOIN profissional p2 ON p.cpf = p2.pessoa_cpf;

-- 6) Consulta usando OUTER JOIN
SELECT * FROM public.usuario u
    FULL OUTER JOIN pessoafisica p ON u.id = p.usuario;

-- 7) Consulta usando função de agregação
-- Quantidade de Usuarios no Sistema
SELECT count(*) AS quantidade_usuarios FROM public.usuario;

-- 8) Consulta usando GROUP BY
-- Quantidade de Profissionais de determinada especialidade
SELECT codigo_cbo , count(id) AS quant_profissionais FROM public.profissional
    GROUP BY codigo_cbo;

-- 9) Consulta usando GROUP BY e HAVING
-- Quantidade de profissionais (maiores ou iguais a 2) de determinada especialidade
SELECT codigo_cbo , count(id) AS quant_profissionais FROM public.profissional
    GROUP BY codigo_cbo HAVING count(id) >= 2;

-- 10) Consulta usando operador IN
SELECT * FROM profissional
         WHERE pessoa_cpf IN
            (SELECT cpf FROM pessoafisica WHERE id >= 2);

-- 11) Consulta usando operador EXISTS

-- 12) Consulta usando operador SOME

-- 13) Consulta usando operador ALL

-- 14) Consulta aninhadas no FROM
