--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Disciplina; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Disciplina" (
    "CodDisciplina" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "CodCurso" character varying(255)
);


ALTER TABLE public."Disciplina" OWNER TO postgres;

--
-- Name: Disciplina_CodDisciplina_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Disciplina_CodDisciplina_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Disciplina_CodDisciplina_seq" OWNER TO postgres;

--
-- Name: Disciplina_CodDisciplina_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Disciplina_CodDisciplina_seq" OWNED BY public."Disciplina"."CodDisciplina";


--
-- Name: Matricula; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Matricula" (
    "NroMatricula" integer NOT NULL,
    "CodDisciplina" character varying(255) NOT NULL,
    "Semestre" character varying(255) NOT NULL,
    "Ano" integer,
    "Nota" integer,
    "NroFaltas" integer
);


ALTER TABLE public."Matricula" OWNER TO postgres;

--
-- Name: Matricula_NroMatricula_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Matricula_NroMatricula_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Matricula_NroMatricula_seq" OWNER TO postgres;

--
-- Name: Matricula_NroMatricula_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Matricula_NroMatricula_seq" OWNED BY public."Matricula"."NroMatricula";


--
-- Name: alunos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alunos (
    "NroMatricula" integer NOT NULL,
    "CPF" character(11) NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "Endereço" character varying(255),
    "Telefone" character(11),
    "Ano Nascimento" integer
);


ALTER TABLE public.alunos OWNER TO postgres;

--
-- Name: alunos_NroMatricula_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."alunos_NroMatricula_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."alunos_NroMatricula_seq" OWNER TO postgres;

--
-- Name: alunos_NroMatricula_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."alunos_NroMatricula_seq" OWNED BY public.alunos."NroMatricula";


--
-- Name: Disciplina CodDisciplina; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Disciplina" ALTER COLUMN "CodDisciplina" SET DEFAULT nextval('public."Disciplina_CodDisciplina_seq"'::regclass);


--
-- Name: Matricula NroMatricula; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Matricula" ALTER COLUMN "NroMatricula" SET DEFAULT nextval('public."Matricula_NroMatricula_seq"'::regclass);


--
-- Name: alunos NroMatricula; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alunos ALTER COLUMN "NroMatricula" SET DEFAULT nextval('public."alunos_NroMatricula_seq"'::regclass);


--
-- Data for Name: Disciplina; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Disciplina" ("CodDisciplina", "Nome", "CodCurso") FROM stdin;
1	Ana	25
\.


--
-- Data for Name: Matricula; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Matricula" ("NroMatricula", "CodDisciplina", "Semestre", "Ano", "Nota", "NroFaltas") FROM stdin;
2	55	2	2005	9	5
\.


--
-- Data for Name: alunos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alunos ("NroMatricula", "CPF", "Nome", "Endereço", "Telefone", "Ano Nascimento") FROM stdin;
\.


--
-- Name: Disciplina_CodDisciplina_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Disciplina_CodDisciplina_seq"', 1, false);


--
-- Name: Matricula_NroMatricula_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Matricula_NroMatricula_seq"', 1, false);


--
-- Name: alunos_NroMatricula_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."alunos_NroMatricula_seq"', 1, false);


--
-- Name: Disciplina Disciplina_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Disciplina"
    ADD CONSTRAINT "Disciplina_pkey" PRIMARY KEY ("CodDisciplina");


--
-- Name: Matricula Matricula_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Matricula"
    ADD CONSTRAINT "Matricula_pkey" PRIMARY KEY ("NroMatricula");


--
-- Name: alunos alunos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alunos
    ADD CONSTRAINT alunos_pkey PRIMARY KEY ("NroMatricula");


--
-- PostgreSQL database dump complete
--

