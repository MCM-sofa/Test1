# -*- coding: utf-8 -*-
"""
Module de tarification pour canapés sur mesure
Gère les calculs de prix TTC et de marges HT
"""

class CanapePricing:
    """
    Classe pour calculer les prix et marges des canapés sur mesure
    """
    
    # ============================================================================
    # PRIX DE VENTE TTC
    # ============================================================================
    
    # Prix des coussins TTC
    PRIX_COUSSINS_TTC = {
        65: 35,
        80: 44,
        90: 48,
        'valise': 70,
        'valise_g': 70,
        'valise_p': 70,
        'valise_pg': 70
    }
    
    # Prix des supports TTC
    PRIX_SUPPORTS_TTC = {
        'banquette_assise': 250,
        'banquette_angle': 250,
        'accoudoir': 225,
        'dossier': 250
    }
    
    # Prix des accessoires TTC
    PRIX_ACCESSOIRES_TTC = {
        'coussin_deco': 15,
        'traversin': 30,
        'surmatelas': 80
    }
    
    # Coefficients pour mousse (prix TTC)
    COEF_MOUSSE_TTC = {
        'D25': 16 * 25,
        'D30': 16 * 30,
        'HR35': 16 * 37,
        'HR45': 16 * 47
    }
    
    # Prix tissu par mètre linéaire TTC
    PRIX_TISSU_PETIT_TTC = 74  # Si largeur+épaisseur*2 <= 140cm
    PRIX_TISSU_GRAND_TTC = 105  # Si largeur+épaisseur*2 > 140cm
    
    # ============================================================================
    # MARGES HT
    # ============================================================================
    
    # Marges des coussins HT
    MARGE_COUSSINS_HT = {
        65: 14,
        80: 17,
        90: 17.5,
        'valise': 25,
        'valise_g': 25,
        'valise_p': 25,
        'valise_pg': 25
    }
    
    # Marges des accessoires HT
    MARGE_ACCESSOIRES_HT = {
        'coussin_deco': 9.5,
        'traversin': 11.6,
        'surmatelas': 31
    }
    
    # Marge accoudoir HT
    MARGE_ACCOUDOIR_HT = 73
    
    # Marge arrondis HT
    MARGE_ARRONDIS_HT = 6.05
    
    # Coefficients pour mousse (marge HT)
    COEF_MOUSSE_MARGE_HT = {
        'D25': 157.5,
        'D30': 188,
        'HR35': 192,
        'HR45': 245
    }
    
    # Prix tissu par mètre linéaire HT (marge)
    PRIX_TISSU_PETIT_MARGE_HT = 11.2
    PRIX_TISSU_GRAND_MARGE_HT = 16.16
    SUPPLEMENT_TISSU_MARGE_HT = 15
    
    # Mousse pré-découpée (marges HT)
    MOUSSE_PREDECOUPEE_HT = {
        '200x70x25': {
            'D25': 42.55,
            'D30': 51,
            'HR35': 65,
            'HR45': 84
        },
        '200x80x25': {
            'D25': 63,
            'D30': 75.20,
            'HR35': 76.20,
            'HR45': 98
        },
        '90x90x25': {
            'D25': 31.9,
            'D30': 38.1,
            'HR35': 38.9,
            'HR45': 49.6
        },
        '100x100x25': {
            'D25': 39.3,
            'D30': 47,
            'HR35': 48,
            'HR45': 61.20
        }
    }
    
    def __init__(self):
        """Initialisation de la classe de pricing"""
        pass
    
    # ============================================================================
    # CALCULS PRIX TTC
    # ============================================================================
    
    def calculer_prix_mousse_tissu_ttc(self, longueur_cm, largeur_cm, epaisseur_cm, type_mousse):
        """
        Calcule le prix TTC de la mousse + tissu pour une banquette
        
        Args:
            longueur_cm: Longueur en cm
            largeur_cm: Largeur en cm
            epaisseur_cm: Épaisseur en cm
            type_mousse: 'D25', 'D30', 'HR35' ou 'HR45'
            
        Returns:
            float: Prix TTC total (mousse + tissu)
        """
        # Prix mousse TTC
        volume_m3 = (longueur_cm * largeur_cm * epaisseur_cm) / 1000000
        coef_mousse = self.COEF_MOUSSE_TTC.get(type_mousse, self.COEF_MOUSSE_TTC['D25'])
        prix_mousse = volume_m3 * coef_mousse
        
        # Prix tissu TTC
        condition_largeur = largeur_cm + (epaisseur_cm * 2)
        if condition_largeur > 140:
            prix_tissu = (longueur_cm / 100) * self.PRIX_TISSU_GRAND_TTC
        else:
            prix_tissu = (longueur_cm / 100) * self.PRIX_TISSU_PETIT_TTC
        
        return prix_mousse + prix_tissu
    
    def calculer_prix_coussin_ttc(self, taille_ou_type):
        """
        Calcule le prix TTC d'un coussin
        
        Args:
            taille_ou_type: 65, 80, 90, 'valise', 'valise_g', 'valise_p', etc.
            
        Returns:
            float: Prix TTC du coussin
        """
        return self.PRIX_COUSSINS_TTC.get(taille_ou_type, 0)
    
    def calculer_prix_support_ttc(self, type_support):
        """
        Calcule le prix TTC d'un support
        
        Args:
            type_support: 'banquette_assise', 'banquette_angle', 'accoudoir', 'dossier'
            
        Returns:
            float: Prix TTC du support
        """
        return self.PRIX_SUPPORTS_TTC.get(type_support, 0)
    
    def calculer_prix_accessoire_ttc(self, type_accessoire):
        """
        Calcule le prix TTC d'un accessoire
        
        Args:
            type_accessoire: 'coussin_deco', 'traversin', 'surmatelas'
            
        Returns:
            float: Prix TTC de l'accessoire
        """
        return self.PRIX_ACCESSOIRES_TTC.get(type_accessoire, 0)
    
    # ============================================================================
    # CALCULS MARGES HT
    # ============================================================================
    
    def calculer_marge_mousse_tissu_ht(self, longueur_cm, largeur_cm, epaisseur_cm, type_mousse):
        """
        Calcule la marge HT de la mousse + tissu pour une banquette
        
        Args:
            longueur_cm: Longueur en cm
            largeur_cm: Largeur en cm
            epaisseur_cm: Épaisseur en cm
            type_mousse: 'D25', 'D30', 'HR35' ou 'HR45'
            
        Returns:
            float: Marge HT totale (mousse + tissu)
        """
        # Marge mousse HT
        volume_m3 = (longueur_cm * largeur_cm * epaisseur_cm) / 1000000
        coef_mousse = self.COEF_MOUSSE_MARGE_HT.get(type_mousse, self.COEF_MOUSSE_MARGE_HT['D25'])
        marge_mousse = volume_m3 * coef_mousse
        
        # Marge tissu HT
        condition_largeur = 2 + largeur_cm + (epaisseur_cm * 2)
        if condition_largeur <= 140:
            marge_tissu = ((longueur_cm / 100) * self.PRIX_TISSU_PETIT_MARGE_HT) + self.SUPPLEMENT_TISSU_MARGE_HT
        else:
            marge_tissu = ((longueur_cm / 100) * self.PRIX_TISSU_GRAND_MARGE_HT) + self.SUPPLEMENT_TISSU_MARGE_HT
        
        return marge_mousse + marge_tissu
    
    def calculer_marge_banquette_ht(self, longueur_cm, est_angle=False):
        """
        Calcule la marge HT d'une banquette (support)
        
        Args:
            longueur_cm: Longueur de la banquette en cm
            est_angle: True si c'est une banquette d'angle
            
        Returns:
            float: Marge HT de la banquette
        """
        if est_angle:
            return 93 + (8 * 1.4)
        elif longueur_cm <= 200:
            return 93 + (8 * 2.5)
        else:
            return 98.5 + 22.5
    
    def calculer_marge_dossier_ht(self, longueur_cm):
        """
        Calcule la marge HT d'un dossier
        
        Args:
            longueur_cm: Longueur du dossier en cm
            
        Returns:
            float: Marge HT du dossier
        """
        if longueur_cm <= 200:
            return 120 + (8 * 4.4)
        else:
            return 132 + (8 * 5.5)
    
    def calculer_marge_accoudoir_ht(self):
        """
        Calcule la marge HT d'un accoudoir
        
        Returns:
            float: Marge HT de l'accoudoir
        """
        return self.MARGE_ACCOUDOIR_HT
    
    def calculer_marge_coussin_ht(self, taille_ou_type):
        """
        Calcule la marge HT d'un coussin
        
        Args:
            taille_ou_type: 65, 80, 90, 'valise', etc.
            
        Returns:
            float: Marge HT du coussin
        """
        return self.MARGE_COUSSINS_HT.get(taille_ou_type, 0)
    
    def calculer_marge_accessoire_ht(self, type_accessoire):
        """
        Calcule la marge HT d'un accessoire
        
        Args:
            type_accessoire: 'coussin_deco', 'traversin', 'surmatelas'
            
        Returns:
            float: Marge HT de l'accessoire
        """
        return self.MARGE_ACCESSOIRES_HT.get(type_accessoire, 0)
    
    def calculer_marge_arrondis_ht(self):
        """
        Calcule la marge HT des arrondis
        
        Returns:
            float: Marge HT des arrondis
        """
        return self.MARGE_ARRONDIS_HT
    
    # ============================================================================
    # CALCUL DEVIS COMPLET
    # ============================================================================
    
    def calculer_devis_complet(self, configuration):
        """
        Calcule un devis complet avec prix TTC et marges HT
        
        Args:
            configuration: Dictionnaire contenant toute la configuration du canapé
                {
                    'banquettes': [{'longueur': 200, 'largeur': 80, 'epaisseur': 25, 'type_mousse': 'D25', 'est_angle': False}, ...],
                    'dossiers': [{'longueur': 200}, ...],
                    'accoudoirs': {'gauche': True, 'droite': True},
                    'coussins': {'65': 4, '80': 2, 'valise': 1},
                    'accessoires': {'coussin_deco': 2, 'traversin': 1, 'surmatelas': 0}
                }
                
        Returns:
            dict: {
                'prix_ttc_total': float,
                'marge_ht_totale': float,
                'benefice_ht': float,  # Prix TTC/1.2 - Marge HT totale
                'details_ttc': {...},
                'details_marge_ht': {...}
            }
        """
        details_ttc = {
            'banquettes_mousse_tissu': 0,
            'supports_banquettes': 0,
            'dossiers': 0,
            'accoudoirs': 0,
            'coussins': 0,
            'accessoires': 0
        }
        
        details_marge_ht = {
            'banquettes_mousse_tissu': 0,
            'supports_banquettes': 0,
            'dossiers': 0,
            'accoudoirs': 0,
            'coussins': 0,
            'accessoires': 0,
            'arrondis': 0
        }
        
        # Calcul banquettes (mousse + tissu + support)
        for banquette in configuration.get('banquettes', []):
            # Prix TTC
            prix_mousse_tissu_ttc = self.calculer_prix_mousse_tissu_ttc(
                banquette['longueur'],
                banquette['largeur'],
                banquette['epaisseur'],
                banquette['type_mousse']
            )
            details_ttc['banquettes_mousse_tissu'] += prix_mousse_tissu_ttc
            
            if banquette.get('est_angle', False):
                details_ttc['supports_banquettes'] += self.PRIX_SUPPORTS_TTC['banquette_angle']
            else:
                details_ttc['supports_banquettes'] += self.PRIX_SUPPORTS_TTC['banquette_assise']
            
            # Marge HT
            marge_mousse_tissu_ht = self.calculer_marge_mousse_tissu_ht(
                banquette['longueur'],
                banquette['largeur'],
                banquette['epaisseur'],
                banquette['type_mousse']
            )
            details_marge_ht['banquettes_mousse_tissu'] += marge_mousse_tissu_ht
            
            marge_support = self.calculer_marge_banquette_ht(
                banquette['longueur'],
                banquette.get('est_angle', False)
            )
            details_marge_ht['supports_banquettes'] += marge_support
        
        # Calcul dossiers
        for dossier in configuration.get('dossiers', []):
            details_ttc['dossiers'] += self.PRIX_SUPPORTS_TTC['dossier']
            marge_dossier = self.calculer_marge_dossier_ht(dossier['longueur'])
            details_marge_ht['dossiers'] += marge_dossier
        
        # Calcul accoudoirs
        accoudoirs = configuration.get('accoudoirs', {})
        nb_accoudoirs = (1 if accoudoirs.get('gauche', False) else 0) + \
                       (1 if accoudoirs.get('droite', False) else 0)
        details_ttc['accoudoirs'] = nb_accoudoirs * self.PRIX_SUPPORTS_TTC['accoudoir']
        details_marge_ht['accoudoirs'] = nb_accoudoirs * self.MARGE_ACCOUDOIR_HT
        
        # Calcul coussins
        for taille, quantite in configuration.get('coussins', {}).items():
            prix_unitaire_ttc = self.calculer_prix_coussin_ttc(taille)
            details_ttc['coussins'] += prix_unitaire_ttc * quantite
            
            marge_unitaire_ht = self.calculer_marge_coussin_ht(taille)
            details_marge_ht['coussins'] += marge_unitaire_ht * quantite
        
        # Calcul accessoires
        for type_acc, quantite in configuration.get('accessoires', {}).items():
            prix_unitaire_ttc = self.calculer_prix_accessoire_ttc(type_acc)
            details_ttc['accessoires'] += prix_unitaire_ttc * quantite
            
            marge_unitaire_ht = self.calculer_marge_accessoire_ht(type_acc)
            details_marge_ht['accessoires'] += marge_unitaire_ht * quantite
        
        # Marge arrondis
        details_marge_ht['arrondis'] = self.MARGE_ARRONDIS_HT
        
        # Totaux
        prix_ttc_total = sum(details_ttc.values())
        marge_ht_totale = sum(details_marge_ht.values())
        
        # Calcul du bénéfice HT
        benefice_ht = (prix_ttc_total / 1.2) - marge_ht_totale
        
        return {
            'prix_ttc_total': round(prix_ttc_total, 2),
            'marge_ht_totale': round(marge_ht_totale, 2),
            'benefice_ht': round(benefice_ht, 2),
            'details_ttc': {k: round(v, 2) for k, v in details_ttc.items()},
            'details_marge_ht': {k: round(v, 2) for k, v in details_marge_ht.items()}
        }
    
    # ============================================================================
    # MÉTHODES UTILITAIRES
    # ============================================================================
    
    def formater_ligne_devis(self, designation, quantite, prix_unitaire, prix_total):
        """
        Formate une ligne de devis
        
        Returns:
            dict: Ligne formatée
        """
        return {
            'designation': designation,
            'quantite': quantite,
            'prix_unitaire': round(prix_unitaire, 2),
            'prix_total': round(prix_total, 2)
        }
    
    def generer_lignes_devis(self, configuration):
        """
        Génère toutes les lignes du devis au format liste
        
        Args:
            configuration: Configuration du canapé
            
        Returns:
            list: Liste de dictionnaires pour chaque ligne
        """
        lignes = []
        
        # Banquettes
        for i, banquette in enumerate(configuration.get('banquettes', []), 1):
            prix = self.calculer_prix_mousse_tissu_ttc(
                banquette['longueur'],
                banquette['largeur'],
                banquette['epaisseur'],
                banquette['type_mousse']
            )
            lignes.append(self.formater_ligne_devis(
                f"Banquette {i} - Mousse {banquette['type_mousse']} + Tissu ({banquette['longueur']}x{banquette['largeur']}x{banquette['epaisseur']}cm)",
                1,
                prix,
                prix
            ))
            
            type_support = 'Banquette d\'angle' if banquette.get('est_angle', False) else 'Support banquette'
            prix_support = self.PRIX_SUPPORTS_TTC['banquette_angle'] if banquette.get('est_angle', False) else self.PRIX_SUPPORTS_TTC['banquette_assise']
            lignes.append(self.formater_ligne_devis(
                type_support,
                1,
                prix_support,
                prix_support
            ))
        
        # Dossiers
        for i, dossier in enumerate(configuration.get('dossiers', []), 1):
            prix = self.PRIX_SUPPORTS_TTC['dossier']
            lignes.append(self.formater_ligne_devis(
                f"Dossier {i} ({dossier['longueur']}cm)",
                1,
                prix,
                prix
            ))
        
        # Accoudoirs
        accoudoirs = configuration.get('accoudoirs', {})
        if accoudoirs.get('gauche', False):
            prix = self.PRIX_SUPPORTS_TTC['accoudoir']
            lignes.append(self.formater_ligne_devis(
                "Accoudoir gauche",
                1,
                prix,
                prix
            ))
        if accoudoirs.get('droite', False):
            prix = self.PRIX_SUPPORTS_TTC['accoudoir']
            lignes.append(self.formater_ligne_devis(
                "Accoudoir droit",
                1,
                prix,
                prix
            ))
        
        # Coussins
        for taille, quantite in configuration.get('coussins', {}).items():
            if quantite > 0:
                prix_unitaire = self.calculer_prix_coussin_ttc(taille)
                designation = f"Coussin valise" if 'valise' in str(taille).lower() else f"Coussin {taille}cm"
                lignes.append(self.formater_ligne_devis(
                    designation,
                    quantite,
                    prix_unitaire,
                    prix_unitaire * quantite
                ))
        
        # Accessoires
        for type_acc, quantite in configuration.get('accessoires', {}).items():
            if quantite > 0:
                prix_unitaire = self.calculer_prix_accessoire_ttc(type_acc)
                designation_map = {
                    'coussin_deco': 'Coussin déco',
                    'traversin': 'Traversin',
                    'surmatelas': 'Surmatelas'
                }
                lignes.append(self.formater_ligne_devis(
                    designation_map.get(type_acc, type_acc),
                    quantite,
                    prix_unitaire,
                    prix_unitaire * quantite
                ))
        
        return lignes


# ============================================================================
# EXEMPLE D'UTILISATION
# ============================================================================

if __name__ == "__main__":
    # Créer une instance du pricing
    pricing = CanapePricing()
    
    # Exemple de configuration de canapé
    config_exemple = {
        'banquettes': [
            {
                'longueur': 200,
                'largeur': 80,
                'epaisseur': 25,
                'type_mousse': 'D25',
                'est_angle': False
            },
            {
                'longueur': 180,
                'largeur': 80,
                'epaisseur': 25,
                'type_mousse': 'D25',
                'est_angle': False
            }
        ],
        'dossiers': [
            {'longueur': 200},
            {'longueur': 180}
        ],
        'accoudoirs': {
            'gauche': True,
            'droite': True
        },
        'coussins': {
            65: 2,
            80: 4,
            'valise': 1
        },
        'accessoires': {
            'coussin_deco': 2,
            'traversin': 1,
            'surmatelas': 0
        }
    }
    
    # Calculer le devis
    devis = pricing.calculer_devis_complet(config_exemple)
    
    print("=" * 60)
    print("DEVIS COMPLET")
    print("=" * 60)
    print(f"\nPrix TTC total: {devis['prix_ttc_total']}€")
    print(f"Marge HT totale: {devis['marge_ht_totale']}€")
    print(f"Bénéfice HT: {devis['benefice_ht']}€")
    
    print("\n" + "-" * 60)
    print("DÉTAILS PRIX TTC:")
    print("-" * 60)
    for cle, valeur in devis['details_ttc'].items():
        print(f"{cle.replace('_', ' ').title()}: {valeur}€")
    
    print("\n" + "-" * 60)
    print("DÉTAILS MARGE HT:")
    print("-" * 60)
    for cle, valeur in devis['details_marge_ht'].items():
        print(f"{cle.replace('_', ' ').title()}: {valeur}€")
    
    print("\n" + "=" * 60)
    
    # Générer les lignes du devis
    lignes = pricing.generer_lignes_devis(config_exemple)
    print("\nLIGNES DU DEVIS:")
    print("-" * 60)
    for ligne in lignes:
        print(f"{ligne['designation']}")
        print(f"  Qté: {ligne['quantite']} | Prix unit: {ligne['prix_unitaire']}€ | Total: {ligne['prix_total']}€")
