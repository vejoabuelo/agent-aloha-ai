#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TESTE DE LÓGICA CORRIGIDA - Sistema FuncionárioIA
Lógica inteligente para capturar nomes completos
"""

import re
import json
from typing import Dict, List, Optional

def detectar_nome_inteligente(content: str) -> Optional[str]:
    """
    LÓGICA SUPER INTELIGENTE PARA DETECTAR NOME COMPLETO
    """
    print(f"🔍 Analisando: '{content}'")
    
    # ESTRATÉGIA 1: Capturar nome completo com tipo
    if 'restaurante' in content.lower():
        # "tenho um restaurante do amor" -> "restaurante do amor"
        match = re.search(r'(?:tenho\s+um\s+|é\s+um\s+)?(restaurante\s+[a-zA-ZÀ-ÿ\s\']{2,30})', content, re.IGNORECASE)
        if match:
            nome = match.group(1).strip()
            print(f"  📍 ESTRATÉGIA 1A: '{nome}'")
            return nome
        
        # "restaurante do amor" -> "restaurante do amor" 
        match = re.search(r'\b(restaurante\s+[a-zA-ZÀ-ÿ\s\']{2,30})', content, re.IGNORECASE)
        if match:
            nome = match.group(1).strip()
            print(f"  📍 ESTRATÉGIA 1B: '{nome}'")
            return nome
    
    # ESTRATÉGIA 2: Nome antes do tipo
    # "amor restaurante" -> "amor restaurante"
    match = re.search(r'\b([a-zA-ZÀ-ÿ\s\']{2,30})\s+(restaurante|pizzaria|loja)', content, re.IGNORECASE)
    if match:
        nome = f"{match.group(1)} {match.group(2)}".strip()
        print(f"  📍 ESTRATÉGIA 2: '{nome}'")
        return nome
    
    # ESTRATÉGIA 3: "se chama" ou "nome é"
    match = re.search(r'(?:se\s+chama|nome\s+é|chamado)\s+([a-zA-ZÀ-ÿ\s\']{2,30})', content, re.IGNORECASE)
    if match:
        nome = match.group(1).strip()
        print(f"  📍 ESTRATÉGIA 3: '{nome}'")
        return nome
    
    # ESTRATÉGIA 4: Entre aspas
    match = re.search(r'"([a-zA-ZÀ-ÿ\s\']{2,30})"', content)
    if match:
        nome = match.group(1).strip()
        print(f"  📍 ESTRATÉGIA 4: '{nome}'")
        return nome
    
    print("  ❌ NENHUMA ESTRATÉGIA FUNCIONOU")
    return None

def teste_deteccao_nomes():
    """
    TESTE ESPECÍFICO DE DETECÇÃO DE NOMES
    """
    print("="*60)
    print("🧪 TESTE ESPECÍFICO - DETECÇÃO DE NOMES")
    print("="*60)
    
    casos_teste = [
        "tenho um restaurante do amor",
        "restaurante do amor",
        "é o amor restaurante", 
        "se chama Pizza Legal",
        "nome é Burguer King",
        "chamado \"Comida Boa\"",
        "meu negócio se chama Pizzaria da Mama"
    ]
    
    for caso in casos_teste:
        print(f"\n📝 TESTE: '{caso}'")
        nome_detectado = detectar_nome_inteligente(caso)
        print(f"✅ RESULTADO: '{nome_detectado}'")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    teste_deteccao_nomes() 