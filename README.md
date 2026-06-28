# Agent-Based Cancer Modeling & Tumor Growth Simulation

A Agent-Based Model (ABM) developed in Python to simulate healthy tissue proliferation, and tumor progression on a 2D 
cell grid. The simulation features real-time graphical rendering (via Pygame) and integrates analytical validation by comparing the simulated growth trajectories against 
a known Gompertz mathematical function used in cancer research.

---

##  Table of Contents
- [Features](#-features)
- [Biological & Mathematical Foundations](#-biological--mathematical-foundations)
- [Project Architecture](#-project-architecture)
- [Prerequisites & Installation](#-prerequisites--installation)
- [Usage & Configuration](#-usage--configuration)
- [Outputs & Data Analysis](#-outputs--data-analysis)
- [References](#-references)

---

##  Features

| Capability                            | Description                                                                                                              |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **Reserach based default parameters** | Probabilistic rules for tumor expansion and healthy tissue proliferation, parameterized from clinical doubling time data. |
| **Memory efficient agent**            | Thin-agent meaning the use of an integer grid instead of full objects , this makes the simulation simple and easy to run. |
| **Pygame GUI**                        | Interactive Pygame rendering with color-coded cell states, dynamic updates, and configurable frame rate.                 |
| **Gompertz Comparison**               | Comparison of simulated tumor growth against the theoretical Gompertz ODE to asses biological accuracy.               |
| **Flexible CLI Interface**            | Fully configurable grid size, time steps, and biological parameters                                                      |

---

##  Biological & Mathematical Foundations

###  Cellular States & Visual Mapping

Each lattice site occupies one of three biologically meaningful states:

| State ID | Biological Interpretation | Pygame Color (RGB) | Visual Appearance |
|----------|---------------------|---------------------|-------------------|
| `0` | Empty space / Extracellular matrix (ECM) | `(103, 49, 71)` | Dark Purple |
| `1` | Healthy tissue | `(255, 105, 180)` | Bright Pink |
| `2` | Tumor mass | `(129, 19, 49)` | Deep Maroon |

###  Grid Interaction & Neighborhood Rules

- **Tumor Initialization**: Tumors are seeded within healthy tissue, surrounded by healthy cells with a variable-thickness randomized border (0–8 pixels) to mimic realistic biological 
margins.
- **Neighborhood Topology**: Von Neumann neighborhood (4-directional: North, South, East, West).
- **Double Grid**: Prevents artifacts from cascading updates by computing new states on a separate layer before committing changes.

###  Growth Kinetics & Biological Scaling

#### Tumor Proliferation (`T_GROWTH_CHANCE`) - Default value
Calibrated to clinical **Hepatocellular Carcinoma (HCC)** volume doubling time (VDT ≈ 140 days)^[Nathani et al., *Gut*, 2021]:

$$
(1 - P)^{140} = 0.5 \implies P = 1 - 0.5^{1/140} \approx 0.00494 \quad (0.494\%/\text{day})
$$



#### Healthy Tissue Proliferation (`C_DOUBLING_TIME`) - Default value
Based on **human hepatocyte kinetics** (doubling time ≈ 48 hours)^[Levy et al., *Nat Biotechnol*, 2015]:
$$
(1 - P)^2 = 0.5 \implies P \approx 0.2929
$$


###  Gompertz Growth Model Verification

To validate emergent macro-dynamics, tumor volume $N(t)$ is compared against the classical Gompertz model:
$$
\frac{dV}{dt} = c * V * ln(\frac{V_{max}}{V})
$$

$c =$ the specific growth rate per t

$V_{max}$ = maximum achievable volume of the tumor, known as the carrying capacity.

$ln(\frac{V_{max}}{V})$ = a natural logarithmic braking factor which drives the growth rate to zero when V apporaches $V_{max}$


##  Project Architecture

```text
project/
├── main.py               # Entry point (orchestrates setup → simulation → analysis)
├── setup.py              # CLI argument parsing, validation, and config generation
├── environment.py        # Core ABM logic: grid updates, neighbor checks, state transitions
├── gui.py                # Pygame rendering, window management, event loop
├── analysis.py           # Gompertz curve fitting, visualization, PDF generation
├── output_writer.py      # CSV serialization of tumor history
└── research_abm.ipynb    # Notebook with biological assumptions & formula derivations
```

---

## ️ Prerequisites & Installation

### System Requirements
- Python ≥ 3.8  
- `pip` package manager

### Installation
```bash
# Clone repository
git clone https://github.com/azzipxonraj/Agent_Based_Cancer_modeling.git
cd Agent_Based_Cancer_modeling

# Install dependencies
pip install pygame matplotlib numpy
```

---

## Usage & Configuration

### Quick Start
```bash
python3 main.py -r 60 -c 60 -t 150
# Equivalent: python3 main.py --rows 60 --cols 60 --max-steps 150
```

###  Command-Line Options

| Short  | Long | Type    | Default | Description                                    |
|--------|------|---------|---------|------------------------------------------------|
| `-r`   | `--rows` | `int`   | `50` | Grid height (rows)                             |
| `-c`   | `--cols` | `int`   | `50` | Grid width (columns)                           |
| `-t`   | `--max-steps` | `int`   | `100` | Max simulation steps (days)                    |
| `-tgc` | `--tumor-growth-chance` | `float` | `0.00494` | Daily tumor proliferation probability          |
| `-cdt` | `--c-doubling-time` | `float` | `0.2928932188` | Healthy tissue daily proliferation probability |
| `-pc`  | `--param-c` | `float` | `0.00494` | Tumor growthspeed constant  (c)                |




---

##  Outputs & Data Analysis

Upon completion or termination, two automated analysis pipelines execute:

### 1. Tumor History Recording
- **File**: `tumor_history.csv`  
- **Content**: Step-by-step tumor cell counts:  
  `step, tumor_count`  
  *(e.g., `0, 25`, `1, 27`, `2, 31`, ...)*

### 2. Gompertz Validation & Visualization
   - **Output**: `tumor_analysis.pdf` — a PDF with 3 pages:
     1. Raw tumorgrowth curve from the ABM simulation
     2. Gompertz prediction
     3. Overlay of simulatie vs. Gompertz model

###  Analysis Workflow
```python
from analysis import gompertz
tumor_counts = load_csv("tumor_history.csv")
theoretical = gompertz(max_steps, N_max, c)

plot(tumor_counts, theoretical)
save_pdf("tumor_analysis.pdf")
```

---

##  References

1. **Yin et al. (2019)**. *A review of mathematical models for tumor dynamics and treatment resistance evolution.* CPT Pharmacometrics & Systems Pharmacology, 8(10), 
720–737.  
2. **Srinivasa et al. (2020)**. *Statistical modelling and machine learning principles for bioinformatics.* Springer Singapore.  
3. **Jain et al. (2014)**. *The Role of Mechanical Forces in Tumor Growth and Therapy.* Annual Review of Biomedical Engineering, 16(1), 321–346.  
4. **Nathani et al. (2021)**. *Hepatocellular carcinoma tumour volume doubling time: a systematic review.* Gut, 70(2), 401–407.5. **Kalra et al. (2023)**. *Physiology, liver.* StatPearls – NCBI Bookshelf.  
6. **Levy et al. (2015)**. *Long-term culture and expansion of primary human hepatocytes.* Nature Biotechnology, 33(12), 1264–1271.

---