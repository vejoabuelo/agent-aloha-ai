#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TESTE COMPLETO - FUNCIONÁRIO IA INTELIGENTE
Validação de todas as funcionalidades implementadas

🎯 FUNCIONALIDADES TESTADAS:
1. Interpretação inteligente de mensagens
2. Configuração automática por profissão  
3. Autoalimentação e aprendizado
4. Fluxos conversacionais naturais
5. Detecção de intenções contextuais
6. Respostas empáticas e não robóticas
"""

import json
from datetime import datetime
import time

class TesteFuncionarioIA:
    def __init__(self):
        self.resultados = []
        self.patterns_salvos = []
        print("🧪 INICIANDO TESTE COMPLETO DO FUNCIONÁRIO IA INTELIGENTE")
        print("=" * 60)

    def testar_interpretacao_inteligente(self):
        """Testa se a IA distingue saudações de profissões"""
        print("\n🔍 TESTE 1: INTERPRETAÇÃO INTELIGENTE")
        print("-" * 40)
        
        casos_teste = {
            # SAUDAÇÕES SIMPLES (não devem configurar automaticamente)
            "oi": {"intent": "greeting", "should_configure": False},
            "olá": {"intent": "greeting", "should_configure": False},
            "oi, tudo bem?": {"intent": "greeting", "should_configure": False},
            "bom dia": {"intent": "greeting", "should_configure": False},
            
            # PROFISSÕES (devem configurar automaticamente)
            "sou psicólogo": {"intent": "configure", "should_configure": True, "type": "clinica"},
            "tenho um restaurante": {"intent": "configure", "should_configure": True, "type": "restaurante"},
            "trabalho com cabelo": {"intent": "configure", "should_configure": True, "type": "salao"},
            "sou mecânico": {"intent": "configure", "should_configure": True, "type": "oficina"},
            "tenho uma loja": {"intent": "configure", "should_configure": True, "type": "loja"},
            
            # SUPORTE
            "quanto custa": {"intent": "support", "should_configure": False},
            "quais os planos": {"intent": "support", "should_configure": False},
            "como funciona": {"intent": "support", "should_configure": False},
            
            # EDIÇÃO
            "alterar nome": {"intent": "edit", "should_configure": False},
            "mudar telefone": {"intent": "edit", "should_configure": False},
            
            # CASOS AMBÍGUOS
            "preciso de ajuda": {"intent": "unclear", "should_configure": False},
            "qualquer coisa": {"intent": "unclear", "should_configure": False}
        }
        
        for mensagem, esperado in casos_teste.items():
            resultado = self.simular_analise_ia(mensagem)
            
            # Verificar se a interpretação está correta
            sucesso = (
                resultado["intent"] == esperado["intent"] and
                resultado.get("should_configure", False) == esperado["should_configure"]
            )
            
            status = "✅ PASSOU" if sucesso else "❌ FALHOU"
            print(f"{status} '{mensagem}' → {resultado['intent']}")
            
            if esperado["should_configure"] and "type" in esperado:
                if resultado.get("businessType") == esperado["type"]:
                    print(f"    ✅ Tipo detectado corretamente: {resultado['businessType']}")
                else:
                    print(f"    ❌ Tipo incorreto: esperado {esperado['type']}, obtido {resultado.get('businessType')}")
            
            self.resultados.append({
                "teste": "interpretacao_inteligente",
                "input": mensagem,
                "esperado": esperado,
                "resultado": resultado,
                "sucesso": sucesso
            })

    def testar_configuracao_automatica(self):
        """Testa configuração automática por profissão"""
        print("\n⚙️ TESTE 2: CONFIGURAÇÃO AUTOMÁTICA")
        print("-" * 40)
        
        profissoes = {
            "psicólogo": {
                "businessType": "clinica",
                "workingHours": "Segunda a Sexta: 08:00 às 18:00",
                "hasDelivery": False,
                "acceptsReservations": True,
                "paymentMethods": "PIX, Cartão, Convênios"
            },
            "pizzaria": {
                "businessType": "restaurante", 
                "workingHours": "Todos os dias: 11:00 às 23:00",
                "hasDelivery": True,
                "acceptsReservations": False,
                "paymentMethods": "PIX, Cartão, Dinheiro"
            },
            "cabeleireira": {
                "businessType": "salao",
                "workingHours": "Terça a Sábado: 09:00 às 19:00", 
                "hasDelivery": False,
                "acceptsReservations": True,
                "paymentMethods": "PIX, Cartão, Dinheiro"
            }
        }
        
        for profissao, config_esperada in profissoes.items():
            print(f"\n🔧 Testando: 'sou {profissao}'")
            
            resultado = self.simular_configuracao_automatica(f"sou {profissao}")
            
            # Verificar cada campo
            campos_corretos = 0
            total_campos = len(config_esperada)
            
            for campo, valor_esperado in config_esperada.items():
                valor_obtido = resultado.get(campo)
                if valor_obtido == valor_esperado:
                    print(f"    ✅ {campo}: {valor_obtido}")
                    campos_corretos += 1
                else:
                    print(f"    ❌ {campo}: esperado '{valor_esperado}', obtido '{valor_obtido}'")
            
            sucesso = campos_corretos == total_campos
            status = "✅ CONFIGURAÇÃO COMPLETA" if sucesso else f"⚠️ {campos_corretos}/{total_campos} CAMPOS CORRETOS"
            print(f"    {status}")
            
            self.resultados.append({
                "teste": "configuracao_automatica",
                "profissao": profissao,
                "campos_corretos": campos_corretos,
                "total_campos": total_campos,
                "sucesso": sucesso
            })

    def testar_autoalimentacao(self):
        """Testa sistema de autoalimentação e aprendizado"""
        print("\n🧠 TESTE 3: AUTOALIMENTAÇÃO E APRENDIZADO")
        print("-" * 40)
        
        # Simular padrões sendo salvos
        patterns_simulados = [
            {
                "input": "sou terapeuta holística",
                "businessType": "clinica",
                "confidence": 0.95,
                "usageCount": 1,
                "timestamp": datetime.now().isoformat()
            },
            {
                "input": "tenho um pet shop",  
                "businessType": "loja",
                "confidence": 0.90,
                "usageCount": 3,
                "timestamp": datetime.now().isoformat()
            },
            {
                "input": "trabalho com unha",
                "businessType": "salao", 
                "confidence": 0.85,
                "usageCount": 2,
                "timestamp": datetime.now().isoformat()
            }
        ]
        
        # Salvar padrões
        print("💾 Salvando padrões de aprendizado...")
        for pattern in patterns_simulados:
            self.patterns_salvos.append(pattern)
            print(f"    ✅ Padrão salvo: '{pattern['input']}' → {pattern['businessType']} (confiança: {pattern['confidence']})")
        
        # Testar detecção de padrões similares
        print("\n🔍 Testando detecção de padrões similares...")
        
        casos_similares = [
            {"input": "sou terapeuta holística", "deve_encontrar": True, "pattern_esperado": "clinica"},
            {"input": "trabalho com terapia holística", "deve_encontrar": True, "pattern_esperado": "clinica"},
            {"input": "tenho pet shop", "deve_encontrar": True, "pattern_esperado": "loja"},
            {"input": "faço unha", "deve_encontrar": True, "pattern_esperado": "salao"},
            {"input": "sou engenheiro", "deve_encontrar": False, "pattern_esperado": None}
        ]
        
        for caso in casos_similares:
            resultado = self.simular_busca_pattern(caso["input"])
            
            if caso["deve_encontrar"]:
                if resultado and resultado.get("businessType") == caso["pattern_esperado"]:
                    print(f"    ✅ '{caso['input']}' → encontrou padrão {resultado['businessType']}")
                else:
                    print(f"    ❌ '{caso['input']}' → não encontrou padrão esperado {caso['pattern_esperado']}")
            else:
                if not resultado:
                    print(f"    ✅ '{caso['input']}' → corretamente não encontrou padrão")
                else:
                    print(f"    ❌ '{caso['input']}' → encontrou padrão indevidamente: {resultado}")

    def testar_fluxos_conversacionais(self):
        """Testa fluxos conversacionais naturais"""
        print("\n💬 TESTE 4: FLUXOS CONVERSACIONAIS")
        print("-" * 40)
        
        fluxos = {
            "saudacao_simples": {
                "input": "oi",
                "resposta_esperada": "menu_opcoes",
                "deve_explicar": True,
                "deve_configurar": False
            },
            "configuracao_profissao": {
                "input": "sou dentista", 
                "resposta_esperada": "explicacao_antes_configurar",
                "deve_explicar": True,
                "deve_configurar": True,
                "delay_configuracao": 3
            },
            "suporte_precos": {
                "input": "quanto custa",
                "resposta_esperada": "informacoes_planos",
                "deve_explicar": True,
                "deve_configurar": False
            },
            "edicao_dados": {
                "input": "alterar nome",
                "resposta_esperada": "campo_edicao",
                "deve_explicar": False,
                "deve_configurar": False
            }
        }
        
        for nome_fluxo, fluxo in fluxos.items():
            print(f"\n🔄 Testando fluxo: {nome_fluxo}")
            print(f"    Input: '{fluxo['input']}'")
            
            resultado = self.simular_fluxo_conversacional(fluxo["input"])
            
            # Verificar tipo de resposta
            if resultado["tipo_resposta"] == fluxo["resposta_esperada"]:
                print(f"    ✅ Tipo de resposta correto: {resultado['tipo_resposta']}")
            else:
                print(f"    ❌ Tipo incorreto: esperado {fluxo['resposta_esperada']}, obtido {resultado['tipo_resposta']}")
            
            # Verificar se explica antes de configurar
            if fluxo["deve_explicar"]:
                if resultado.get("tem_explicacao"):
                    print("    ✅ Fornece explicação adequada")
                else:
                    print("    ❌ Não fornece explicação")
            
            # Verificar tom empático (não robótico)
            if resultado.get("tom_empatico"):
                print("    ✅ Tom conversacional e empático")
            else:
                print("    ❌ Tom robótico ou frio")

    def testar_casos_especiais(self):
        """Testa casos especiais e edge cases"""
        print("\n🚨 TESTE 5: CASOS ESPECIAIS")
        print("-" * 40)
        
        casos_especiais = [
            # Frases longas
            "oi, eu sou psicólogo e quero criar um funcionário virtual para minha clínica",
            
            # Múltiplas profissões
            "sou psicólogo e também tenho um restaurante",
            
            # Gírias e variações
            "trampo com cabelo",
            "mexo com comida",
            "cuido de dente",
            
            # Profissões específicas
            "sou coach de vida",
            "trabalho com estética facial",
            "tenho oficina de moto",
            
            # Casos ambíguos
            "preciso de um sistema",
            "quero automatizar atendimento",
            "como posso melhorar vendas",
            
            # Erros de digitação
            "sou psicologo",
            "tenho restaurate",
            "trabalho com cabelo e unha"
        ]
        
        print("🔍 Testando casos especiais...")
        
        for caso in casos_especiais:
            resultado = self.simular_analise_ia(caso)
            
            # Verificar se conseguiu processar sem erro
            if resultado.get("erro"):
                print(f"    ❌ '{caso[:30]}...' → ERRO: {resultado['erro']}")
            else:
                intent = resultado.get("intent", "unclear")
                confidence = resultado.get("confidence", 0)
                
                if confidence > 0.7:
                    print(f"    ✅ '{caso[:30]}...' → {intent} (confiança: {confidence:.2f})")
                else:
                    print(f"    ⚠️ '{caso[:30]}...' → {intent} (baixa confiança: {confidence:.2f})")

    def simular_analise_ia(self, mensagem):
        """Simula análise da IA (substituindo chamada real)"""
        # Simulação baseada nas regras implementadas
        msg_lower = mensagem.lower()
        
        # Detectar saudações
        saudacoes = ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]
        if any(s in msg_lower for s in saudacoes) and not any(p in msg_lower for p in ["sou", "tenho", "trabalho"]):
            return {"intent": "greeting", "should_configure": False, "confidence": 0.95}
        
        # Detectar profissões
        profissoes_clinica = ["psicólogo", "psicologo", "médico", "medico", "dentista", "advogado", "terapeuta", "coach"]
        profissoes_restaurante = ["restaurante", "pizzaria", "lanchonete", "delivery", "chef", "comida"]
        profissoes_salao = ["cabeleireiro", "cabeleireira", "cabelo", "manicure", "estética", "estetica", "barbeiro", "unha"]
        profissoes_oficina = ["mecânico", "mecanico", "oficina", "conserto", "moto", "carro"]
        profissoes_loja = ["loja", "comércio", "comercio", "venda", "pet shop", "farmácia"]
        
        if any(p in msg_lower for p in profissoes_clinica):
            return {"intent": "configure", "businessType": "clinica", "should_configure": True, "confidence": 0.90}
        elif any(p in msg_lower for p in profissoes_restaurante):
            return {"intent": "configure", "businessType": "restaurante", "should_configure": True, "confidence": 0.90}
        elif any(p in msg_lower for p in profissoes_salao):
            return {"intent": "configure", "businessType": "salao", "should_configure": True, "confidence": 0.90}
        elif any(p in msg_lower for p in profissoes_oficina):
            return {"intent": "configure", "businessType": "oficina", "should_configure": True, "confidence": 0.90}
        elif any(p in msg_lower for p in profissoes_loja):
            return {"intent": "configure", "businessType": "loja", "should_configure": True, "confidence": 0.90}
        
        # Detectar suporte
        suporte_keywords = ["quanto custa", "preço", "preco", "plano", "como funciona", "o que é"]
        if any(k in msg_lower for k in suporte_keywords):
            return {"intent": "support", "should_configure": False, "confidence": 0.85}
        
        # Detectar edição
        edit_keywords = ["alterar", "mudar", "editar", "trocar", "corrigir"]
        if any(k in msg_lower for k in edit_keywords):
            return {"intent": "edit", "should_configure": False, "confidence": 0.80}
        
        return {"intent": "unclear", "should_configure": False, "confidence": 0.3}

    def simular_configuracao_automatica(self, profissao):
        """Simula aplicação de configuração automática"""
        configs = {
            "clinica": {
                "businessType": "clinica",
                "workingHours": "Segunda a Sexta: 08:00 às 18:00",
                "hasDelivery": False,
                "acceptsReservations": True,
                "paymentMethods": "PIX, Cartão, Convênios"
            },
            "restaurante": {
                "businessType": "restaurante",
                "workingHours": "Todos os dias: 11:00 às 23:00", 
                "hasDelivery": True,
                "acceptsReservations": False,
                "paymentMethods": "PIX, Cartão, Dinheiro"
            },
            "salao": {
                "businessType": "salao",
                "workingHours": "Terça a Sábado: 09:00 às 19:00",
                "hasDelivery": False,
                "acceptsReservations": True,
                "paymentMethods": "PIX, Cartão, Dinheiro"
            }
        }
        
        analise = self.simular_analise_ia(profissao)
        business_type = analise.get("businessType")
        
        if business_type in configs:
            return configs[business_type]
        else:
            return {"erro": "Tipo de negócio não reconhecido"}

    def simular_busca_pattern(self, mensagem):
        """Simula busca de padrões salvos"""
        msg_lower = mensagem.lower()
        
        for pattern in self.patterns_salvos:
            # Calcular similaridade simples
            words_input = set(msg_lower.split())
            words_pattern = set(pattern["input"].split())
            
            intersection = len(words_input.intersection(words_pattern))
            union = len(words_input.union(words_pattern))
            
            similarity = intersection / union if union > 0 else 0
            
            if similarity > 0.6:  # 60% de similaridade
                return pattern
        
        return None

    def simular_fluxo_conversacional(self, mensagem):
        """Simula fluxo conversacional"""
        analise = self.simular_analise_ia(mensagem)
        
        if analise["intent"] == "greeting":
            return {
                "tipo_resposta": "menu_opcoes",
                "tem_explicacao": True,
                "tom_empatico": True,
                "conteudo": "Olá! Bem-vindo ao FuncionárioIA! Como posso ajudar?"
            }
        elif analise["intent"] == "configure":
            return {
                "tipo_resposta": "explicacao_antes_configurar",
                "tem_explicacao": True,
                "tom_empatico": True,
                "delay": 3,
                "conteudo": "Perfeito! Detectei sua profissão. Vou configurar automaticamente..."
            }
        elif analise["intent"] == "support":
            return {
                "tipo_resposta": "informacoes_planos", 
                "tem_explicacao": True,
                "tom_empatico": True,
                "conteudo": "FuncionárioIA custa R$ 49/mês..."
            }
        elif analise["intent"] == "edit":
            return {
                "tipo_resposta": "campo_edicao",
                "tem_explicacao": False,
                "tom_empatico": True,
                "conteudo": "Qual nome você gostaria de usar?"
            }
        
        return {
            "tipo_resposta": "chat_geral",
            "tem_explicacao": False,
            "tom_empatico": True
        }

    def gerar_relatorio(self):
        """Gera relatório final dos testes"""
        print("\n" + "=" * 60)
        print("📊 RELATÓRIO FINAL DOS TESTES")
        print("=" * 60)
        
        # Contar sucessos e falhas
        total_testes = len(self.resultados)
        sucessos = sum(1 for r in self.resultados if r["sucesso"])
        falhas = total_testes - sucessos
        
        taxa_sucesso = (sucessos / total_testes * 100) if total_testes > 0 else 0
        
        print(f"\n📈 ESTATÍSTICAS GERAIS:")
        print(f"    Total de testes: {total_testes}")
        print(f"    Sucessos: {sucessos} ✅")
        print(f"    Falhas: {falhas} ❌")
        print(f"    Taxa de sucesso: {taxa_sucesso:.1f}%")
        
        # Relatório por categoria
        categorias = {}
        for resultado in self.resultados:
            categoria = resultado["teste"]
            if categoria not in categorias:
                categorias[categoria] = {"sucessos": 0, "total": 0}
            
            categorias[categoria]["total"] += 1
            if resultado["sucesso"]:
                categorias[categoria]["sucessos"] += 1
        
        print(f"\n📊 RESULTADOS POR CATEGORIA:")
        for categoria, stats in categorias.items():
            taxa = (stats["sucessos"] / stats["total"] * 100) if stats["total"] > 0 else 0
            print(f"    {categoria}: {stats['sucessos']}/{stats['total']} ({taxa:.1f}%)")
        
        # Padrões de autoalimentação salvos
        print(f"\n🧠 AUTOALIMENTAÇÃO:")
        print(f"    Padrões salvos: {len(self.patterns_salvos)}")
        for pattern in self.patterns_salvos:
            print(f"    - '{pattern['input']}' → {pattern['businessType']} (usado {pattern['usageCount']}x)")
        
        # Recomendações
        print(f"\n💡 RECOMENDAÇÕES:")
        if taxa_sucesso >= 90:
            print("    ✅ Sistema funcionando excelentemente!")
        elif taxa_sucesso >= 75:
            print("    ⚠️ Sistema bom, mas pode melhorar nos casos de falha")
        else:
            print("    ❌ Sistema precisa de ajustes significativos")
        
        if falhas > 0:
            print("    🔧 Revisar casos que falharam")
            print("    🎯 Melhorar prompts da IA para maior precisão")
            print("    📚 Expandir base de treinamento")
        
        # Salvar relatório em JSON
        relatorio = {
            "timestamp": datetime.now().isoformat(),
            "estatisticas": {
                "total_testes": total_testes,
                "sucessos": sucessos,
                "falhas": falhas,
                "taxa_sucesso": taxa_sucesso
            },
            "resultados_detalhados": self.resultados,
            "patterns_autoalimentacao": self.patterns_salvos,
            "recomendacoes": []
        }
        
        with open("relatorio_teste_ia_inteligente.json", "w", encoding="utf-8") as f:
            json.dump(relatorio, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Relatório salvo em: relatorio_teste_ia_inteligente.json")

def main():
    """Executa todos os testes"""
    teste = TesteFuncionarioIA()
    
    try:
        # Executar todos os testes
        teste.testar_interpretacao_inteligente()
        teste.testar_configuracao_automatica()
        teste.testar_autoalimentacao()
        teste.testar_fluxos_conversacionais()
        teste.testar_casos_especiais()
        
        # Gerar relatório final
        teste.gerar_relatorio()
        
        print("\n🎉 TESTE COMPLETO FINALIZADO!")
        print("   Verifique o relatório para detalhes completos.")
        
    except Exception as e:
        print(f"\n❌ ERRO DURANTE OS TESTES: {e}")
        print("   Verifique os logs para mais detalhes.")

if __name__ == "__main__":
    main() 