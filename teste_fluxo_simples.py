#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TESTE FLUXO SIMPLES - Sistema FuncionárioIA
Versão sem emojis para compatibilidade Windows
"""

import re
from typing import Dict, List, Optional

class AgentData:
    def __init__(self):
        self.businessName = "Como vai ser o nome do seu"
        self.businessType = ""
        self.contactPhone = "(xx) xxxxx-xxxx"
        self.location = "Endereco a ser definido"
        self.services = "Lista de servicos sera criada automaticamente"
        self.workingHours = ""
        self.paymentMethods = ""
        self.personality = ""

    def get_completion_status(self):
        total_fields = 8
        completed = 0
        missing = []
        
        if self.businessName and len(self.businessName) > 3 and "nome do seu" not in self.businessName.lower():
            completed += 1
        else:
            missing.append("NOME")
            
        if self.businessType:
            completed += 1
        else:
            missing.append("TIPO")
            
        if self.contactPhone and "xxxxx" not in self.contactPhone and len(self.contactPhone) >= 10:
            completed += 1
        else:
            missing.append("TELEFONE")
            
        if self.location and "ser definido" not in self.location.lower() and len(self.location) > 5:
            completed += 1
        else:
            missing.append("ENDERECO")
            
        if self.services and "sera criada" not in self.services.lower():
            completed += 1
        else:
            missing.append("SERVICOS")
            
        if self.workingHours:
            completed += 1
        else:
            missing.append("HORARIOS")
            
        if self.paymentMethods:
            completed += 1
        else:
            missing.append("PAGAMENTO")
            
        if self.personality:
            completed += 1
        else:
            missing.append("PERSONALIDADE")
        
        percentage = int((completed / total_fields) * 100)
        return percentage, missing

class FuncionarioIASimulator:
    def __init__(self):
        self.agent_data = AgentData()
        
    def detectar_nome_inteligente(self, content: str) -> Optional[str]:
        print(f"    Detectando nome em: '{content}'")
        
        # ESTRATEGIA 1: "nome e X" ou "se chama X" 
        match = re.search(r'(?:nome\s+(?:é|do\w*)\s*|se\s+chama\s+|chamado\s+|chama\s+)([a-zA-ZÀ-ÿ\s\']{2,40})', content, re.IGNORECASE)
        if match:
            nome = match.group(1).strip()
            nome = re.sub(r'\s*(?:restaurante|pizzaria|loja|oficina|clinica)$', '', nome, flags=re.IGNORECASE)
            if len(nome) >= 3:
                print(f"    ESTRATEGIA 1 (nome e/se chama): '{nome}'")
                return nome
        
        # ESTRATEGIA 2: "restaurante do amor"
        if any(tipo in content.lower() for tipo in ['restaurante', 'pizzaria']):
            match = re.search(r'(?:tenho\s+um\s+|é\s+um\s+)?(restaurante\s+[a-zA-ZÀ-ÿ\s\']{2,30})', content, re.IGNORECASE)
            if match:
                nome = match.group(1).strip()
                print(f"    ESTRATEGIA 2A: '{nome}'")
                return nome
        
        print("    NENHUMA ESTRATEGIA FUNCIONOU")
        return None

    def analisar_e_atualizar(self, content: str) -> Dict:
        text = content.lower()
        updates = {}
        saved_something = False
        
        print(f"  ANALISE: '{content}'")
        
        # TEMPLATES PRIMEIRO
        if (('restaurante' in text or 'pizza' in text) and not self.agent_data.businessType):
            print("    APLICANDO TEMPLATE RESTAURANTE...")
            updates['businessType'] = 'restaurante'
            updates['personality'] = 'amigavel, carinhoso e atencioso'
            updates['workingHours'] = 'Segunda a Domingo: 10h as 23h'
            updates['paymentMethods'] = 'PIX, Cartao de credito, Cartao de debito, Dinheiro'
            updates['services'] = 'Cardapio variado, Delivery, Balcao, Reservas disponiveis'
            saved_something = True
            
            # Aplicar ao objeto
            for key, value in updates.items():
                setattr(self.agent_data, key, value)
        
        # DETECCAO DE NOME
        if (not self.agent_data.businessName or 
            len(self.agent_data.businessName) < 3 or 
            "nome do seu" in self.agent_data.businessName.lower()):
            
            nome_detectado = self.detectar_nome_inteligente(content)
            if nome_detectado and 3 <= len(nome_detectado) <= 50:
                updates['businessName'] = nome_detectado
                self.agent_data.businessName = nome_detectado
                saved_something = True
                print(f"    NOME SALVO: '{nome_detectado}'")
        
        # DETECCAO DE TELEFONE
        if (not self.agent_data.contactPhone or 
            "xxxxx" in self.agent_data.contactPhone or 
            len(self.agent_data.contactPhone) < 10):
            
            match = re.search(r'(\d{10,11})', content)
            if match:
                telefone = match.group(1)
                if telefone != '11987654321':
                    updates['contactPhone'] = telefone
                    self.agent_data.contactPhone = telefone
                    saved_something = True
                    print(f"    TELEFONE SALVO: '{telefone}'")
        
        print(f"  SALVOU ALGO: {saved_something}")
        return {'updates': updates, 'saved_something': saved_something}

    def simular_conversa(self, mensagens_usuario: List[str]) -> None:
        print(f"\n{'='*60}")
        print("SIMULACAO DE CONVERSA COMPLETA")
        print(f"{'='*60}")
        
        for i, mensagem in enumerate(mensagens_usuario):
            print(f"\nTURNO {i+1}")
            print(f"USUARIO: '{mensagem}'")
            
            resultado = self.analisar_e_atualizar(mensagem)
            percentage, missing = self.agent_data.get_completion_status()
            print(f"STATUS: {percentage}% completo - Faltam: {missing}")
            
            if percentage == 100:
                print("\nCONFIGURACAO COMPLETA!")
                break

def teste_restaurante():
    print("TESTE: CONFIGURAR RESTAURANTE")
    simulator = FuncionarioIASimulator()
    
    mensagens = [
        "tenho um restaurante do amor",
        "o telefone e 11987654322",
        "fica na rua das flores 123"
    ]
    
    simulator.simular_conversa(mensagens)
    return simulator.agent_data

if __name__ == "__main__":
    print("TESTE SIMPLES - FUNCIONARIO IA")
    
    restaurante = teste_restaurante()
    perc, missing = restaurante.get_completion_status()
    
    print(f"\nRESULTADO FINAL:")
    print(f"RESTAURANTE: {perc}% completo - {restaurante.businessName}")
    
    if perc >= 75:
        print("SUCESSO! LOGICA FUNCIONANDO")
    else:
        print("ERRO! LOGICA COM PROBLEMAS") 