# -*- coding: utf-8 -*-
"""
Application Streamlit pour générer des devis de canapés sur mesure
Utilise le module canape_pricing.py
"""

import streamlit as st
from canape_pricing import CanapePricing

# Configuration de la page
st.set_page_config(
    page_title="Devis Canapés Sur Mesure",
    page_icon="🛋️",
    layout="wide"
)

# Initialiser le pricing
pricing = CanapePricing()

# ============================================================================
# TITRE ET DESCRIPTION
# ============================================================================

st.title("🛋️ Générateur de Devis - Canapés Sur Mesure")
st.markdown("---")

# ============================================================================
# FORMULAIRE DE CONFIGURATION
# ============================================================================

st.header("📝 Configuration du canapé")

# Créer deux colonnes pour le formulaire
col_form1, col_form2 = st.columns(2)

with col_form1:
    # ========================================================================
    # SECTION BANQUETTES
    # ========================================================================
    st.subheader("1️⃣ Banquettes")
    nb_banquettes = st.number_input(
        "Nombre de banquettes",
        min_value=1,
        max_value=5,
        value=2,
        help="Nombre de sections de banquettes pour votre canapé"
    )
    
    banquettes = []
    for i in range(nb_banquettes):
        with st.expander(f"⚙️ Banquette {i+1}", expanded=(i == 0)):
            col1, col2 = st.columns(2)
            
            with col1:
                longueur = st.number_input(
                    "Longueur (cm)",
                    min_value=50,
                    max_value=300,
                    value=200,
                    step=5,
                    key=f"long_{i}"
                )
                largeur = st.number_input(
                    "Largeur (cm)",
                    min_value=50,
                    max_value=150,
                    value=80,
                    step=5,
                    key=f"larg_{i}"
                )
            
            with col2:
                epaisseur = st.number_input(
                    "Épaisseur (cm)",
                    min_value=10,
                    max_value=40,
                    value=25,
                    step=5,
                    key=f"ep_{i}"
                )
                type_mousse = st.selectbox(
                    "Type de mousse",
                    ['D25', 'D30', 'HR35', 'HR45'],
                    key=f"mousse_{i}",
                    help="D25/D30: Densité | HR35/HR45: Haute Résilience"
                )
            
            est_angle = st.checkbox(
                "🔄 Banquette d'angle",
                key=f"angle_{i}",
                help="Cochez si cette banquette est en angle"
            )
            
            banquettes.append({
                'longueur': longueur,
                'largeur': largeur,
                'epaisseur': epaisseur,
                'type_mousse': type_mousse,
                'est_angle': est_angle
            })
    
    # ========================================================================
    # SECTION DOSSIERS
    # ========================================================================
    st.subheader("2️⃣ Dossiers")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        dossier_gauche = st.checkbox("◀️ Dossier gauche")
        if dossier_gauche:
            long_gauche = st.number_input(
                "Longueur (cm)",
                min_value=50,
                max_value=300,
                value=200,
                step=5,
                key="dos_g"
            )
    
    with col2:
        dossier_bas = st.checkbox("🔽 Dossier bas")
        if dossier_bas:
            long_bas = st.number_input(
                "Longueur (cm)",
                min_value=50,
                max_value=300,
                value=200,
                step=5,
                key="dos_b"
            )
    
    with col3:
        dossier_droit = st.checkbox("▶️ Dossier droit")
        if dossier_droit:
            long_droit = st.number_input(
                "Longueur (cm)",
                min_value=50,
                max_value=300,
                value=200,
                step=5,
                key="dos_d"
            )
    
    dossiers = []
    if dossier_gauche:
        dossiers.append({'longueur': long_gauche})
    if dossier_bas:
        dossiers.append({'longueur': long_bas})
    if dossier_droit:
        dossiers.append({'longueur': long_droit})
    
    # ========================================================================
    # SECTION ACCOUDOIRS
    # ========================================================================
    st.subheader("3️⃣ Accoudoirs")
    
    col1, col2 = st.columns(2)
    
    with col1:
        accoudoir_gauche = st.checkbox("◀️ Accoudoir gauche")
    
    with col2:
        accoudoir_droit = st.checkbox("▶️ Accoudoir droit")
    
    accoudoirs = {
        'gauche': accoudoir_gauche,
        'droite': accoudoir_droit
    }

with col_form2:
    # ========================================================================
    # SECTION COUSSINS
    # ========================================================================
    st.subheader("4️⃣ Coussins")
    
    col1, col2 = st.columns(2)
    
    with col1:
        coussin_65 = st.number_input(
            "Coussins 65cm",
            min_value=0,
            max_value=20,
            value=0,
            help="Prix unitaire: 35€ TTC"
        )
        coussin_80 = st.number_input(
            "Coussins 80cm",
            min_value=0,
            max_value=20,
            value=0,
            help="Prix unitaire: 44€ TTC"
        )
    
    with col2:
        coussin_90 = st.number_input(
            "Coussins 90cm",
            min_value=0,
            max_value=20,
            value=0,
            help="Prix unitaire: 48€ TTC"
        )
        coussin_valise = st.number_input(
            "Coussins valise",
            min_value=0,
            max_value=20,
            value=0,
            help="Prix unitaire: 70€ TTC"
        )
    
    coussins = {}
    if coussin_65 > 0:
        coussins[65] = coussin_65
    if coussin_80 > 0:
        coussins[80] = coussin_80
    if coussin_90 > 0:
        coussins[90] = coussin_90
    if coussin_valise > 0:
        coussins['valise'] = coussin_valise
    
    # ========================================================================
    # SECTION ACCESSOIRES
    # ========================================================================
    st.subheader("5️⃣ Accessoires")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        coussin_deco = st.number_input(
            "Coussins déco",
            min_value=0,
            max_value=20,
            value=0,
            help="Prix unitaire: 15€ TTC"
        )
    
    with col2:
        traversin = st.number_input(
            "Traversins",
            min_value=0,
            max_value=10,
            value=0,
            help="Prix unitaire: 30€ TTC"
        )
    
    with col3:
        surmatelas = st.number_input(
            "Surmatelas",
            min_value=0,
            max_value=5,
            value=0,
            help="Prix unitaire: 80€ TTC"
        )
    
    accessoires = {
        'coussin_deco': coussin_deco,
        'traversin': traversin,
        'surmatelas': surmatelas
    }

st.markdown("---")

# ============================================================================
# CALCUL DU DEVIS
# ============================================================================

configuration = {
    'banquettes': banquettes,
    'dossiers': dossiers,
    'accoudoirs': accoudoirs,
    'coussins': coussins,
    'accessoires': accessoires
}

devis = pricing.calculer_devis_complet(configuration)

# ============================================================================
# AFFICHAGE DES RÉSULTATS
# ============================================================================

st.header("💰 Résultats du devis")

# Affichage des totaux
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Prix TTC Total",
        f"{devis['prix_ttc_total']}€",
        help="Prix de vente total TTC"
    )

with col2:
    st.metric(
        "Marge HT Totale",
        f"{devis['marge_ht_totale']}€",
        help="Coût total HT de fabrication"
    )

with col3:
    benefice_pourcent = (devis['benefice_ht'] / (devis['prix_ttc_total'] / 1.2)) * 100 if devis['prix_ttc_total'] > 0 else 0
    st.metric(
        "Bénéfice HT",
        f"{devis['benefice_ht']}€",
        delta=f"{benefice_pourcent:.1f}%",
        help="Bénéfice = (Prix TTC / 1.2) - Marge HT"
    )

st.markdown("---")

# ============================================================================
# DÉTAILS DU DEVIS
# ============================================================================

st.subheader("📋 Détail du devis")

# Créer un tableau pour les lignes du devis
lignes = pricing.generer_lignes_devis(configuration)

if lignes:
    # En-tête du tableau
    col1, col2, col3, col4 = st.columns([5, 1, 2, 2])
    with col1:
        st.markdown("**Désignation**")
    with col2:
        st.markdown("**Qté**")
    with col3:
        st.markdown("**Prix unit. TTC**")
    with col4:
        st.markdown("**Total TTC**")
    
    st.markdown("---")
    
    # Lignes du devis
    for ligne in lignes:
        col1, col2, col3, col4 = st.columns([5, 1, 2, 2])
        with col1:
            st.write(ligne['designation'])
        with col2:
            st.write(f"× {ligne['quantite']}")
        with col3:
            st.write(f"{ligne['prix_unitaire']}€")
        with col4:
            st.write(f"**{ligne['prix_total']}€**")
    
    st.markdown("---")
    
    # Total final
    col1, col2, col3, col4 = st.columns([5, 1, 2, 2])
    with col4:
        st.markdown(f"### **{devis['prix_ttc_total']}€**")
else:
    st.info("Configurez votre canapé pour voir le devis détaillé.")

st.markdown("---")

# ============================================================================
# RÉPARTITION DES COÛTS (GRAPHIQUE)
# ============================================================================

st.subheader("📊 Répartition des coûts")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Prix TTC par catégorie**")
    details_ttc = devis['details_ttc']
    for categorie, montant in details_ttc.items():
        if montant > 0:
            pourcentage = (montant / devis['prix_ttc_total']) * 100 if devis['prix_ttc_total'] > 0 else 0
            st.write(f"• {categorie.replace('_', ' ').title()}: {montant}€ ({pourcentage:.1f}%)")

with col2:
    st.markdown("**Marge HT par catégorie**")
    details_marge = devis['details_marge_ht']
    for categorie, montant in details_marge.items():
        if montant > 0:
            pourcentage = (montant / devis['marge_ht_totale']) * 100 if devis['marge_ht_totale'] > 0 else 0
            st.write(f"• {categorie.replace('_', ' ').title()}: {montant}€ ({pourcentage:.1f}%)")

st.markdown("---")

# ============================================================================
# BOUTONS D'ACTION
# ============================================================================

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("🖨️ Générer le PDF", type="primary", use_container_width=True):
        st.info("Fonction de génération PDF à implémenter avec ReportLab ou similaire")

with col2:
    if st.button("📧 Envoyer par email", use_container_width=True):
        st.info("Fonction d'envoi par email à implémenter")

with col3:
    if st.button("💾 Sauvegarder", use_container_width=True):
        st.info("Fonction de sauvegarde à implémenter")

# ============================================================================
# PIED DE PAGE
# ============================================================================

st.markdown("---")
st.caption("Application de devis pour canapés sur mesure | Version 1.0")
