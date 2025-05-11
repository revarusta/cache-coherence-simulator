print("Simulasi cache coherence dimulai!")

from simulator import simulate

def main():
    print("\n==============================")
    print("      CACHE SIMULATOR")
    print("==============================\n")
    
    # Simulasi dengan protokol koherensi (MSI)
    print(">>> Menjalankan simulasi DENGAN koherensi cache (MSI)...")
    simulate(use_coherence=True)

    # Simulasi tanpa protokol koherensi
    print(">>> Menjalankan simulasi TANPA koherensi cache...")
    simulate(use_coherence=False)

if __name__ == "__main__":
    main()
