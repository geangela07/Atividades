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
-- Name: Compra; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Compra" (
    "ID" integer NOT NULL,
    "ID_Empresa" integer NOT NULL,
    "ID_Fornecedor" integer NOT NULL,
    "Data_Pedido" date DEFAULT CURRENT_DATE NOT NULL
);


ALTER TABLE public."Compra" OWNER TO postgres;

--
-- Name: Compra_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Compra" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Compra_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Empresa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Empresa" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "Endereço" character varying(255) NOT NULL,
    "CNPJ" character(14) NOT NULL
);


ALTER TABLE public."Empresa" OWNER TO postgres;

--
-- Name: Empresa_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Empresa" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Empresa_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Fornecedor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Fornecedor" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "CNPJ" character(14) NOT NULL,
    "Endereço" character varying(255)
);


ALTER TABLE public."Fornecedor" OWNER TO postgres;

--
-- Name: Fornecedor_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Fornecedor" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Fornecedor_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: Compra; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Compra" ("ID", "ID_Empresa", "ID_Fornecedor", "Data_Pedido") FROM stdin;
\.


--
-- Data for Name: Empresa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Empresa" ("ID", "Nome", "Endereço", "CNPJ") FROM stdin;
1	Once	741258963125963	Rua gggg      
\.


--
-- Data for Name: Fornecedor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Fornecedor" ("ID", "Nome", "CNPJ", "Endereço") FROM stdin;
1	Angelo	96325874112365	\N
\.


--
-- Name: Compra_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Compra_ID_seq"', 1, true);


--
-- Name: Empresa_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Empresa_ID_seq"', 1, true);


--
-- Name: Fornecedor_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Fornecedor_ID_seq"', 1, true);


--
-- Name: Compra Compra_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Compra"
    ADD CONSTRAINT "Compra_pkey" PRIMARY KEY ("ID");


--
-- Name: Empresa Empresa_CNPJ_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Empresa"
    ADD CONSTRAINT "Empresa_CNPJ_key" UNIQUE ("CNPJ");


--
-- Name: Empresa Empresa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Empresa"
    ADD CONSTRAINT "Empresa_pkey" PRIMARY KEY ("ID");


--
-- Name: Fornecedor Fornecedor_CNPJ_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Fornecedor"
    ADD CONSTRAINT "Fornecedor_CNPJ_key" UNIQUE ("CNPJ");


--
-- Name: Fornecedor Fornecedor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Fornecedor"
    ADD CONSTRAINT "Fornecedor_pkey" PRIMARY KEY ("ID");


--
-- Name: Compra fk_empresa; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Compra"
    ADD CONSTRAINT fk_empresa FOREIGN KEY ("ID_Empresa") REFERENCES public."Empresa"("ID");


--
-- Name: Compra fk_fornecedor; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Compra"
    ADD CONSTRAINT fk_fornecedor FOREIGN KEY ("ID_Fornecedor") REFERENCES public."Fornecedor"("ID");


--
-- PostgreSQL database dump complete
--

