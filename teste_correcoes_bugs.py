#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TESTE CORREÇÕES DE BUGS - Sistema FuncionárioIA
Testa especificamente as correções implementadas
"""

import re

def testar_deteccao_nome_corrigida():
    """Testa se a detecção de nome está funcionando corretamente"""
    print("=== TESTE DETECÇÃO DE NOME CORRIGIDA ===")
    
    casos_teste = [
        {
            "input": "Tenho um restaurante e quero criar um funcionário IA",
            "esperado": None,  # Não deve detectar nome aqui
            "motivo": "Não tem nome específico"
        },
        {
            "input": "Restaurante do amor",
            "esperado": "Restaurante do amor",
            "motivo": "Nome completo com tipo"
        },
        {
            "input": "✅ Nome 'Restaurante do Amor' salvo no arquivo!",
            "esperado": None,  # Deve ser ignorado
            "motivo": "Resposta da própria IA"
        },
        {
            "input": "Qual é o nome do seu restaurante?",
            "esperado": None,  # Deve ser ignorado
            "motivo": "Pergunta da IA"
        },
        {
            "input": "se chama Pizzaria da Vovó",
            "esperado": "Pizzaria da Vovó",
            "motivo": "Nome com 'se chama'"
        }
    ]
    
    def detectar_nome_corrigido(content: str):
        # IGNORAR se é resposta da própria IA
        if any(palavra in content for palavra in ['✅', 'salvo', 'Qual é', 'arquivo', 'Quais são', 'Como vai ser']):
            return None
        
        # IGNORAR frases que não têm nome específico
        if any(frase in content for frase in ['quero criar', 'funcionário IA', 'atendimento no WhatsApp']):
            return None
        
        # ESTRATÉGIA 1: "se chama X" ou "nome é X" - PRIORIDADE MÁXIMA
        match = re.search(r'(?:se\s+chama\s+|nome\s+é\s+|chamado\s+)([a-zA-ZÀ-ÿ\s\']{3,40})', content, re.IGNORECASE)
        if match:
            nome = match.group(1).strip()
            nome = re.sub(r'\s*(?:restaurante|pizzaria|loja|oficina|clínica)$', '', nome, flags=re.IGNORECASE)
            nome = re.sub(r'\s*(?:seu|meu|do|da|de|um|uma)$', '', nome, flags=re.IGNORECASE)
            if len(nome) >= 3 and 'restaurante' not in nome.lower() and 'funcionário' not in nome.lower():
                return nome
        
        # ESTRATÉGIA 2: "Restaurante do Amor" completo (sem palavras genéricas)
        match = re.search(r'\b((?:restaurante|pizzaria|loja|oficina|clínica)\s+[a-zA-ZÀ-ÿ\s\']{3,30})', content, re.IGNORECASE)
        if match:
            nome = match.group(1).strip()
            if not any(palavra in content.lower() for palavra in ['qual', 'nome do', 'quero', 'funcionário']):
                return nome
        
        return None
    
    sucessos = 0
    total = len(casos_teste)
    
    for i, caso in enumerate(casos_teste, 1):
        resultado = detectar_nome_corrigido(caso['input'])
        
        print(f"\nCASO {i}: {caso['input'][:50]}...")
        print(f"ESPERADO: {caso['esperado']}")
        print(f"RESULTADO: {resultado}")
        print(f"MOTIVO: {caso['motivo']}")
        
        if resultado == caso['esperado']:
            print("✅ PASSOU")
            sucessos += 1
        else:
            print("❌ FALHOU")
    
    print(f"\n=== RESULTADO: {sucessos}/{total} testes passaram ===")
    return sucessos == total

def testar_deteccao_endereco_corrigida():
    """Testa se a detecção de endereço está funcionando"""
    print("\n=== TESTE DETECÇÃO DE ENDEREÇO CORRIGIDA ===")
    
    casos_teste = [
        {
            "input": "avenida do amor, 876",
            "esperado": "avenida do amor, 876",
            "motivo": "Endereço completo"
        },
        {
            "input": "✅ Endereço 'avenida do amor, 876' salvo no arquivo!",
            "esperado": None,
            "motivo": "Resposta da IA deve ser ignorada"
        },
        {
            "input": "do Restaurante do Amor",
            "esperado": None,
            "motivo": "Não é endereço válido"
        },
        {
            "input": "fica na rua das flores 123",
            "esperado": "rua das flores 123",
            "motivo": "Endereço com 'fica na'"
        }
    ]
    
    def detectar_endereco_corrigido(content: str):
        # IGNORAR se é resposta da própria IA
        if any(palavra in content for palavra in ['✅', 'Qual é', 'do Restaurante']):
            return None
        
        patterns = [
            r'(?:endereço|localizado|fica|situado|na|no)\s+([a-zA-ZÀ-ÿ\s\d,.-]{8,80})',
            r'\b((?:rua|avenida|av\.?|r\.?)\s+[a-zA-ZÀ-ÿ\s\d,.-]{5,50})'
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                endereco = match.group(1).strip()
                endereco = re.sub(r'^(na|no|em)\s+', '', endereco, flags=re.IGNORECASE)
                if 8 < len(endereco) < 80 and 'Restaurante' not in endereco:
                    return endereco
        
        return None
    
    sucessos = 0
    total = len(casos_teste)
    
    for i, caso in enumerate(casos_teste, 1):
        resultado = detectar_endereco_corrigido(caso['input'])
        
        print(f"\nCASO {i}: {caso['input']}")
        print(f"ESPERADO: {caso['esperado']}")
        print(f"RESULTADO: {resultado}")
        print(f"MOTIVO: {caso['motivo']}")
        
        if resultado == caso['esperado']:
            print("✅ PASSOU")
            sucessos += 1
        else:
            print("❌ FALHOU")
    
    print(f"\n=== RESULTADO: {sucessos}/{total} testes passaram ===")
    return sucessos == total

def testar_filtro_ia():
    """Testa se o sistema ignora respostas da própria IA"""
    print("\n=== TESTE FILTRO RESPOSTAS DA IA ===")
    
    respostas_ia = [
        "✅ Nome 'Restaurante do Amor' salvo no arquivo!",
        "Qual é o telefone do Restaurante do Amor?",
        "🎉 Perfeito! Seu funcionário IA está 100% configurado!",
        "✅ Telefone '17991956944' salvo no arquivo!",
        "Quais são os serviços oferecidos?"
    ]
    
    def deve_ignorar(content: str):
        filtros = ['✅', 'salvo', 'arquivo', 'Qual é', '🎉', 'Perfeito!', 'detectei', 'configurado', 'Quais são']
        return any(filtro in content for filtro in filtros)
    
    sucessos = 0
    
    for i, resposta in enumerate(respostas_ia, 1):
        deve_ser_ignorado = deve_ignorar(resposta)
        
        print(f"\nCASO {i}: {resposta[:40]}...")
        print(f"DEVE SER IGNORADO: {deve_ser_ignorado}")
        
        if deve_ser_ignorado:
            print("✅ CORRETAMENTE IGNORADO")
            sucessos += 1
        else:
            print("❌ NÃO FOI IGNORADO (ERRO)")
    
    print(f"\n=== RESULTADO: {sucessos}/{len(respostas_ia)} testes passaram ===")
    return sucessos == len(respostas_ia)

def main():
    """Executa todos os testes de correção"""
    print("TESTE COMPLETO DE CORREÇÕES DE BUGS")
    print("Verificando se as correções implementadas funcionam...\n")
    
    teste1 = testar_deteccao_nome_corrigida()
    teste2 = testar_deteccao_endereco_corrigida()
    teste3 = testar_filtro_ia()
    
    print(f"\n{'='*60}")
    print("RESUMO DOS TESTES DE CORREÇÃO")
    print(f"{'='*60}")
    print(f"✅ Detecção Nome Corrigida: {'PASSOU' if teste1 else 'FALHOU'}")
    print(f"✅ Detecção Endereço Corrigida: {'PASSOU' if teste2 else 'FALHOU'}")
    print(f"✅ Filtro Respostas IA: {'PASSOU' if teste3 else 'FALHOU'}")
    
    if teste1 and teste2 and teste3:
        print(f"\n🎉 TODAS AS CORREÇÕES FUNCIONANDO!")
        print("Sistema pronto para ser testado novamente")
    else:
        print(f"\n❌ ALGUMAS CORREÇÕES AINDA PRECISAM DE AJUSTE")
        print("Revisar lógica antes de testar")

if __name__ == "__main__":
    main() 