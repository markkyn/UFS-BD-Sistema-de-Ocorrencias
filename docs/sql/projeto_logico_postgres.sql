-- PostgreSQL Script
-- Mon Aug 14 09:49:25 2023

-- Table Usuario
CREATE TABLE IF NOT EXISTS public.Usuario (
  id SERIAL PRIMARY KEY,
  email VARCHAR(45),
  senha VARCHAR(45),
  data_cadastro DATE,
  last_login TIMESTAMPTZ
);

-- Table PessoaFisica
CREATE TABLE IF NOT EXISTS public.PessoaFisica (
  cpf SERIAL PRIMARY KEY,
  data_nasc DATE NOT NULL,
  primeiro_nome VARCHAR(45),
  sobrenome VARCHAR(45),
  usuario INT REFERENCES public.Usuario(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  UNIQUE(cpf)
);

-- Table Profissional
CREATE TABLE IF NOT EXISTS public.Profissional (
  id INT PRIMARY KEY,
  pessoa_cpf INT NOT NULL REFERENCES public.PessoaFisica(cpf) ON DELETE NO ACTION ON UPDATE NO ACTION,
  codigo_cbo VARCHAR(45)
);

-- Table Gestor
CREATE TABLE IF NOT EXISTS public.Gestor (
  profissional_id INT PRIMARY KEY REFERENCES public.Profissional(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  nivel_de_acesso INT
);

-- Table TipoOperador
CREATE TABLE IF NOT EXISTS public.TipoOperador (
  id INT PRIMARY KEY,
  nome VARCHAR(45)
);

-- Table Operacional
CREATE TABLE IF NOT EXISTS public.Operacional (
  profissional_id INT PRIMARY KEY REFERENCES public.Profissional(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  tipo_operador_id INT REFERENCES public.TipoOperador(id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Table Solicitante
CREATE TABLE IF NOT EXISTS public.Solicitante (
  profissional_id INT PRIMARY KEY REFERENCES public.Profissional(id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Table Ocorrência
CREATE TABLE IF NOT EXISTS public.Ocorrencia (
  id INT PRIMARY KEY,
  data_criacao TIMESTAMPTZ,
  prioridade VARCHAR(20),
  solicitante_id INT REFERENCES public.Solicitante(profissional_id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Table Endereço
CREATE TABLE IF NOT EXISTS public.Endereco (
  id INT PRIMARY KEY,
  rua VARCHAR(45),
  bairro VARCHAR(45),
  cep VARCHAR(45)
);

-- Table Atendimento
CREATE TABLE IF NOT EXISTS public.Atendimento (
  id INT PRIMARY KEY,
  datahora_atendimento TIMESTAMPTZ,
  tipo_servico VARCHAR(45),
  ocorrencia_id INT REFERENCES public.Ocorrencia(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  endereco_id INT REFERENCES public.Endereco(id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Table Instituição
CREATE TABLE IF NOT EXISTS public.Instituicao (
  id INT PRIMARY KEY,
  nome VARCHAR(45),
  gestora INT REFERENCES public.Instituicao(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  endereco INT REFERENCES public.Endereco(id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Table TipoRelatório
CREATE TABLE IF NOT EXISTS public.TipoRelatorio (
  id INT PRIMARY KEY,
  nome VARCHAR(45)
);

-- Table Relatório
CREATE TABLE IF NOT EXISTS public.Relatorio (
  identificador INT PRIMARY KEY,
  atendimento_id INT REFERENCES public.Atendimento(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  tipo_relatorio_id INT REFERENCES public.TipoRelatorio(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  texto VARCHAR(256)
);

-- Table VinculoProfissional
CREATE TABLE IF NOT EXISTS public.VinculoProfissional (
  id INT PRIMARY KEY,
  profissional_id INT REFERENCES public.Profissional(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  instituicao_id INT REFERENCES public.Instituicao(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  is_active SMALLINT
);

-- Table Operacional_Atendimento
CREATE TABLE IF NOT EXISTS public.Operacional_Atendimento (
  id INT PRIMARY KEY,
  id_operacional INT REFERENCES public.Operacional(profissional_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  id_atendimento INT REFERENCES public.Atendimento(id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Table Telefone
CREATE TABLE IF NOT EXISTS public.Telefone (
  id SERIAL PRIMARY KEY,
  telefone VARCHAR(9),
  DDD SMALLINT,
  country SMALLINT,
  pessoa INT REFERENCES public.PessoaFisica(cpf) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Placeholder table for view view1
CREATE TABLE IF NOT EXISTS public.view1 (id INT);

-- View view1
DROP TABLE IF EXISTS public.view1;
