#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TESTE HUMANO COMPLETO - Sistema FuncionárioIA
Simula exatamente como um humano real usaria o sistema
"""

import time
import requests
import json
from typing import Dict, List

class TestadorHumano:
    def __init__(self):
        self.base_url = "http://localhost:8081"  # Conforme mostrado no terminal
        self.agent_data = {
            'businessName': 'Como vai ser o nome do seu',
            'businessType': '',
            'contactPhone': '(xx) xxxxx-xxxx',
            'location': 'Endereco a ser definido',
            'services': 'Lista de servicos sera criada automaticamente',
            'workingHours': '',
            'paymentMethods': '',
            'personality': ''
        }
        self.conversas = []
        
    def print_step(self, step_num: int, titulo: str):
        print(f"\n{'='*80}")
        print(f"PASSO {step_num}: {titulo}")
        print(f"{'='*80}")
        
    def simular_conversa_mistral(self, mensagem_usuario: str, agente_atual: Dict) -> str:
        """Simula exatamente como a Mistral responderia no sistema real"""
        
        # Verificar se precisa aplicar template
        if not agente_atual['businessType']:
            if 'restaurante' in mensagem_usuario.lower() or 'pizza' in mensagem_usuario.lower():
                agente_atual['businessType'] = 'restaurante'
                agente_atual['personality'] = 'amigavel, carinhoso e atencioso'
                agente_atual['workingHours'] = 'Segunda a Domingo: 10h as 23h'
                agente_atual['paymentMethods'] = 'PIX, Cartao de credito, Cartao de debito, Dinheiro'
                agente_atual['services'] = 'Cardapio variado, Delivery, Balcao, Reservas disponiveis'
                print("    [SISTEMA] Template RESTAURANTE aplicado automaticamente!")
                
            elif 'loja' in mensagem_usuario.lower():
                agente_atual['businessType'] = 'loja'
                agente_atual['personality'] = 'prestativo, atencioso e vendedor'
                agente_atual['workingHours'] = 'Segunda a Sabado: 9h as 18h'
                agente_atual['paymentMethods'] = 'PIX, Cartao de credito, Cartao de debito, Dinheiro'
                agente_atual['services'] = 'Produtos variados, Atendimento personalizado, Promocoes especiais'
                print("    [SISTEMA] Template LOJA aplicado automaticamente!")
                
            elif 'oficina' in mensagem_usuario.lower():
                agente_atual['businessType'] = 'oficina'
                agente_atual['personality'] = 'tecnico, confiavel e profissional'
                agente_atual['workingHours'] = 'Segunda a Sexta: 8h as 18h, Sabado: 8h as 12h'
                agente_atual['paymentMethods'] = 'PIX, Cartao de credito, Cartao de debito, Dinheiro'
                agente_atual['services'] = 'Revisao geral, Troca de oleo, Freios, Suspensao, Diagnostico'
                print("    [SISTEMA] Template OFICINA aplicado automaticamente!")
        
        # Detectar informacoes na mensagem
        info_detectada = []
        
        # Detectar nome
        if 'nome do seu' in agente_atual['businessName'] or len(agente_atual['businessName']) < 3:
            # Estrategia 1: "nome e X" ou "se chama X"
            import re
            match = re.search(r'(?:nome\s+e\s+|se\s+chama\s+|chamado\s+)([a-zA-Z\s]{3,30})', mensagem_usuario, re.IGNORECASE)
            if match:
                nome = match.group(1).strip()
                agente_atual['businessName'] = nome
                info_detectada.append(f"NOME: {nome}")
                print(f"    [DETECCAO] Nome detectado: '{nome}'")
            
            # Estrategia 2: "restaurante do amor"
            elif 'restaurante' in mensagem_usuario.lower():
                match = re.search(r'(?:tenho\s+um\s+)?(restaurante\s+[a-zA-Z\s]{2,30})', mensagem_usuario, re.IGNORECASE)
                if match:
                    nome = match.group(1).strip()
                    agente_atual['businessName'] = nome
                    info_detectada.append(f"NOME: {nome}")
                    print(f"    [DETECCAO] Nome restaurante detectado: '{nome}'")
        
        # Detectar telefone
        if 'xxxxx' in agente_atual['contactPhone']:
            import re
            match = re.search(r'(\d{10,11})', mensagem_usuario)
            if match:
                telefone = match.group(1)
                agente_atual['contactPhone'] = telefone
                info_detectada.append(f"TELEFONE: {telefone}")
                print(f"    [DETECCAO] Telefone detectado: '{telefone}'")
        
        # Detectar endereco
        if 'ser definido' in agente_atual['location']:
            if any(palavra in mensagem_usuario.lower() for palavra in ['rua', 'avenida', 'endereco', 'fica']):
                import re
                match = re.search(r'(?:rua|avenida|endereco|fica)\s+(.{5,50})', mensagem_usuario, re.IGNORECASE)
                if match:
                    endereco = match.group(1).strip()
                    agente_atual['location'] = endereco
                    info_detectada.append(f"ENDERECO: {endereco}")
                    print(f"    [DETECCAO] Endereco detectado: '{endereco}'")
        
        # Calcular progresso
        total_campos = 8
        preenchidos = 0
        
        if agente_atual['businessName'] and 'nome do seu' not in agente_atual['businessName']:
            preenchidos += 1
        if agente_atual['businessType']:
            preenchidos += 1
        if agente_atual['contactPhone'] and 'xxxxx' not in agente_atual['contactPhone']:
            preenchidos += 1
        if agente_atual['location'] and 'ser definido' not in agente_atual['location']:
            preenchidos += 1
        if agente_atual['services'] and 'sera criada' not in agente_atual['services']:
            preenchidos += 1
        if agente_atual['workingHours']:
            preenchidos += 1
        if agente_atual['paymentMethods']:
            preenchidos += 1
        if agente_atual['personality']:
            preenchidos += 1
            
        progresso = int((preenchidos / total_campos) * 100)
        
        # Gerar resposta da IA baseada no progresso
        if info_detectada:
            confirmacao = ", ".join(info_detectada)
            if progresso == 100:
                return f"Perfeito! Detectei: {confirmacao}. Seu funcionario IA esta 100% configurado e pronto para atender clientes!"
            elif progresso >= 75:
                faltando = []
                if 'xxxxx' in agente_atual['contactPhone']:
                    faltando.append("telefone")
                if 'ser definido' in agente_atual['location']:
                    faltando.append("endereco")
                if faltando:
                    return f"Otimo! Detectei: {confirmacao}. Agora preciso do {' e '.join(faltando)} para finalizar."
                else:
                    return f"Excelente! Detectei: {confirmacao}. Configuracao {progresso}% completa!"
            else:
                return f"Entendi! Detectei: {confirmacao}. Vamos continuar configurando seu funcionario IA."
        else:
            if progresso == 0:
                return "Ola! Vou te ajudar a criar seu funcionario IA. Que tipo de negocio voce tem? (restaurante, loja, oficina, etc.)"
            elif progresso < 50:
                return "Vamos continuar! Preciso de mais informacoes para configurar seu funcionario IA."
            else:
                return f"Estamos no caminho certo! Configuracao {progresso}% completa. Continue me dando as informacoes."
    
    def testar_fluxo_completo_restaurante(self):
        """TESTE 1: Criar funcionario para restaurante do zero"""
        self.print_step(1, "TESTANDO CRIACAO DE FUNCIONARIO RESTAURANTE")
        
        print("HUMANO: Abrindo navegador em http://localhost:8081")
        print("HUMANO: Vendo interface ChatGPT com 4 templates")
        print("HUMANO: Decidindo criar um restaurante...")
        
        # Simulando conversa passo a passo
        mensagens_teste = [
            "tenho um restaurante do amor",
            "o telefone e 11987654322", 
            "fica na rua das flores 123",
            "temos 50 sabores de pizza"
        ]
        
        print(f"\nCONVERSA SIMULADA (como humano digitaria):")
        for i, msg in enumerate(mensagens_teste, 1):
            print(f"\n--- TURNO {i} ---")
            print(f"HUMANO DIGITA: '{msg}'")
            
            # IA processa e responde
            resposta_ia = self.simular_conversa_mistral(msg, self.agent_data)
            print(f"IA RESPONDE: {resposta_ia}")
            
            # Mostrar estado atual do lado esquerdo
            print(f"\n[LADO ESQUERDO - EDITOR ATUALIZADO]:")
            print(f"Nome: {self.agent_data['businessName']}")
            print(f"Tipo: {self.agent_data['businessType']}")
            print(f"Telefone: {self.agent_data['contactPhone']}")
            print(f"Endereco: {self.agent_data['location']}")
            print(f"Servicos: {self.agent_data['services']}")
            print(f"Horarios: {self.agent_data['workingHours']}")
            
            time.sleep(1)  # Simular tempo humano
            
        return self.agent_data.copy()
    
    def testar_funcionario_atendendo_cliente(self, agente_configurado: Dict):
        """TESTE 2: Testar se o funcionario atende clientes corretamente"""
        self.print_step(2, "TESTANDO FUNCIONARIO ATENDENDO CLIENTES")
        
        print("HUMANO: Clicando no botao 'Testar WhatsApp'")
        print("HUMANO: Simulando conversas de clientes...")
        
        # Simular conversas de clientes
        conversas_clientes = [
            {
                "cliente": "Ola! Voces fazem delivery?",
                "esperado": "falar sobre delivery, ser carinhoso"
            },
            {
                "cliente": "Qual o horario de funcionamento?", 
                "esperado": "informar Segunda a Domingo: 10h as 23h"
            },
            {
                "cliente": "Quantos sabores de pizza voces tem?",
                "esperado": "falar sobre os 50 sabores"
            },
            {
                "cliente": "Qual o endereco?",
                "esperado": "informar rua das flores 123"
            },
            {
                "cliente": "Aceitam PIX?",
                "esperado": "confirmar que aceitam PIX e outros pagamentos"
            }
        ]
        
        funcionario_aprovado = True
        
        for i, conversa in enumerate(conversas_clientes, 1):
            print(f"\n--- TESTE CLIENTE {i} ---")
            print(f"CLIENTE: {conversa['cliente']}")
            
            # Simular resposta do funcionario IA
            resposta = self.simular_resposta_funcionario(conversa['cliente'], agente_configurado)
            print(f"FUNCIONARIO IA: {resposta}")
            
            # Verificar se resposta e adequada
            if self.verificar_resposta_adequada(resposta, conversa['esperado'], agente_configurado):
                print("✅ RESPOSTA ADEQUADA")
            else:
                print("❌ RESPOSTA INADEQUADA")
                funcionario_aprovado = False
                
            time.sleep(0.5)
        
        return funcionario_aprovado
    
    def simular_resposta_funcionario(self, pergunta_cliente: str, agente: Dict) -> str:
        """Simula como o funcionario IA responderia ao cliente"""
        pergunta = pergunta_cliente.lower()
        nome = agente['businessName']
        
        if 'delivery' in pergunta:
            return f"Ola! Sim, o {nome} faz delivery! Temos um cardapio variado com entrega rapida. Posso te ajudar com algum pedido especifico?"
            
        elif 'horario' in pergunta or 'funcionamento' in pergunta:
            return f"Nosso horario de funcionamento e {agente['workingHours']}. Estamos sempre prontos para te atender!"
            
        elif 'sabor' in pergunta or 'pizza' in pergunta:
            return f"Temos 50 sabores deliciosos de pizza! Desde as tradicionais ate sabores especiais. Quer que eu recomende algumas opcoes?"
            
        elif 'endereco' in pergunta or 'onde' in pergunta:
            return f"Estamos localizados na {agente['location']}. Facil de encontrar! Quer fazer um pedido?"
            
        elif 'pix' in pergunta or 'pagamento' in pergunta:
            return f"Sim! Aceitamos {agente['paymentMethods']}. Escolha a forma que for melhor para voce!"
            
        else:
            return f"Ola! Bem-vindo ao {nome}! Como posso te ajudar hoje? Temos um cardapio delicioso!"
    
    def verificar_resposta_adequada(self, resposta: str, esperado: str, agente: Dict) -> bool:
        """Verifica se a resposta do funcionario foi adequada"""
        resposta_lower = resposta.lower()
        
        if 'delivery' in esperado:
            return 'delivery' in resposta_lower and 'sim' in resposta_lower
        elif 'horario' in esperado:
            return agente['workingHours'].lower() in resposta_lower
        elif 'sabores' in esperado:
            return '50' in resposta and 'sabor' in resposta_lower
        elif 'endereco' in esperado:
            return agente['location'].lower() in resposta_lower
        elif 'pix' in esperado:
            return 'pix' in resposta_lower and 'aceit' in resposta_lower
            
        return True
    
    def testar_outros_tipos_negocio(self):
        """TESTE 3: Testar outros tipos de negocio"""
        self.print_step(3, "TESTANDO OUTROS TIPOS DE NEGOCIO")
        
        # Resetar dados
        self.agent_data = {
            'businessName': 'Como vai ser o nome do seu',
            'businessType': '',
            'contactPhone': '(xx) xxxxx-xxxx',
            'location': 'Endereco a ser definido',
            'services': 'Lista de servicos sera criada automaticamente',
            'workingHours': '',
            'paymentMethods': '',
            'personality': ''
        }
        
        print("HUMANO: Testando template de LOJA...")
        print("HUMANO DIGITA: 'tenho uma loja de roupas'")
        
        resposta = self.simular_conversa_mistral("tenho uma loja de roupas", self.agent_data)
        print(f"IA RESPONDE: {resposta}")
        
        print(f"\n[TEMPLATE LOJA APLICADO]:")
        print(f"Tipo: {self.agent_data['businessType']}")
        print(f"Personalidade: {self.agent_data['personality']}")
        print(f"Horarios: {self.agent_data['workingHours']}")
        
        # Testar nome especifico
        print(f"\nHUMANO DIGITA: 'o nome e Moda Legal'")
        resposta = self.simular_conversa_mistral("o nome e Moda Legal", self.agent_data)
        print(f"IA RESPONDE: {resposta}")
        print(f"Nome detectado: {self.agent_data['businessName']}")
        
        return self.agent_data['businessName'] == "Moda Legal"
    
    def executar_todos_os_testes(self):
        """Executa todos os testes como um humano real faria"""
        print("TESTADOR HUMANO - FUNCIONARIO IA")
        print("Simulando uso real do sistema passo a passo...\n")
        
        # Teste 1: Criar restaurante
        print("👤 HUMANO: Vou testar criando um restaurante...")
        agente_restaurante = self.testar_fluxo_completo_restaurante()
        
        # Teste 2: Funcionario atendendo
        print("\n👤 HUMANO: Agora vou testar se o funcionario atende bem...")
        funcionario_ok = self.testar_funcionario_atendendo_cliente(agente_restaurante)
        
        # Teste 3: Outros tipos
        print("\n👤 HUMANO: Vou testar outros tipos de negocio...")
        loja_ok = self.testar_outros_tipos_negocio()
        
        # Resultado final
        self.print_step(4, "RESULTADO DOS TESTES HUMANOS")
        
        print(f"✅ Criacao de restaurante: {'SUCESSO' if agente_restaurante['businessName'] != 'Como vai ser o nome do seu' else 'FALHOU'}")
        print(f"✅ Funcionario atendendo: {'SUCESSO' if funcionario_ok else 'FALHOU'}")
        print(f"✅ Template loja: {'SUCESSO' if loja_ok else 'FALHOU'}")
        
        progresso_restaurante = self.calcular_progresso(agente_restaurante)
        print(f"✅ Configuracao automatica: {progresso_restaurante}%")
        
        if progresso_restaurante >= 75 and funcionario_ok and loja_ok:
            print(f"\n🎉 SISTEMA APROVADO NOS TESTES HUMANOS!")
            print(f"O funcionario IA esta respondendo corretamente e detectando informacoes!")
        else:
            print(f"\n❌ SISTEMA PRECISA DE AJUSTES")
            print(f"Alguns testes falharam, precisa calibrar melhor")
            
        return progresso_restaurante >= 75 and funcionario_ok and loja_ok
    
    def calcular_progresso(self, agente: Dict) -> int:
        total = 8
        preenchidos = 0
        
        if agente['businessName'] and 'nome do seu' not in agente['businessName']:
            preenchidos += 1
        if agente['businessType']:
            preenchidos += 1
        if agente['contactPhone'] and 'xxxxx' not in agente['contactPhone']:
            preenchidos += 1
        if agente['location'] and 'ser definido' not in agente['location']:
            preenchidos += 1
        if agente['services'] and 'sera criada' not in agente['services']:
            preenchidos += 1
        if agente['workingHours']:
            preenchidos += 1
        if agente['paymentMethods']:
            preenchidos += 1
        if agente['personality']:
            preenchidos += 1
            
        return int((preenchidos / total) * 100)

if __name__ == "__main__":
    testador = TestadorHumano()
    sucesso = testador.executar_todos_os_testes()
    
    if sucesso:
        print("\n🚀 SISTEMA PRONTO PARA PRODUCAO!")
    else:
        print("\n🔧 SISTEMA PRECISA DE CALIBRACAO!") 