import time
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BANDS = ["N77", "N78", "B3", "B1"]

def run_vran_node():
    logging.info("vRAN Node Service Initialized. Starting cell site monitoring...")
    while True:
        band = random.choice(BANDS)
        ber = round(random.uniform(0.0001, 0.05), 4)
        status = "HEALTHY" if ber < 0.03 else "DEGRADED - High BER"
        
        logging.info(f"Node: vDU-01 | Band: {band} | BER: {ber} | Status: {status}")
        time.sleep(5)

if __name__ == "__main__":
    run_vran_node()
