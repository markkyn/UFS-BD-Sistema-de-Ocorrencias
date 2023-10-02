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
-- cpf de todos os profissionais que sao ativos em pelo menos uma instituicao
SELECT pessoa_cpf FROM profissional p
    WHERE EXISTS (SELECT NULL FROM vinculoprofissional vp WHERE p.id = vp.profissional_id AND vp.is_active = true);

-- 12) Consulta usando operador SOME
-- Nome completo das pessoas que possuem algum telefone que nao e brasileiro
SELECT primeiro_nome, sobrenome FROM pessoafisica pf
    WHERE pf.cpf = SOME (SELECT pessoa FROM telefone t WHERE t.country <> 55);

-- 13) Consulta usando operador ALL
-- Instituicoes onde todos os profissionais sao ativos
SELECT nome FROM instituicao i
    WHERE true = ALL (SELECT is_active FROM vinculoprofissional vp WHERE i.id = vp.instituicao_id);

-- 14) Consulta aninhadas no FROM
-- Instituicoes cujo endereco já foi passivo de atendimento
SELECT nome, rua, bairro FROM (SELECT i.nome, e.rua, e.bairro, i.endereco FROM endereco e INNER JOIN instituicao i ON e.id = i.endereco) x
    WHERE EXISTS (SELECT NULL FROM atendimento a WHERE a.endereco_id = x.endereco);