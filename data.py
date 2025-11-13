projects = [
    {
        "id": 1,
        "title": "FEA of Stress Concentrations (Academic Project)",
        "description": "Objective: To validate theoretical stress calculations against Finite Element Analysis (FEA) simulations for components with geometric discontinuities.",
        "details": """Project Overview:
I conducted a structured analysis using ANSYS to simulate stress concentrations in three key components: a plate with a hole, a notched beam, and a stepped shaft. The project systematically bridged textbook theory with practical simulation to ensure design reliability.

Key Actions & Results:
- Modeled & Simulated: Created and analyzed parametric models under load.
- Validated with Theory: Calculated theoretical stress concentration factors (Kt) and nominal stresses by hand, then cross-referenced them with FEA results.
- Achieved Correlation: Confirmed FEA results aligned with theoretical predictions, observing stress multipliers of 2-3x in critical areas.

Skills Demonstrated:
ANSYS FEA (Static Structural), Stress Analysis, Parametric Modeling, Hand Calculation Validation.

Conclusion:
This project honed my ability to use CAE tools as a verified engineering platform, underscoring the importance of accurately predicting stress concentrations to prevent mechanical failure.""",
        "images": ["1.jpg"],
        "pdf": "FEA_Stress_Concentration.pdf"
    },
    {
        "id": 2,
        "title": "Automotive Suspension Assembly Redesign (Comprehensive FEA Project)",
        "description": "Objective: To redesign an automobile suspension assembly for significant weight reduction while maintaining structural integrity and safety.",
        "details": """Project Overview:
I led a comprehensive Finite Element Analysis project to optimize a suspension lower arm and strut. The process involved iterative design, material selection (Titanium and Aluminum alloys), and validation under static and dynamic loads.

Key Actions & Results:
- Optimized Design: Executed three design iterations, progressing from a mixed-material assembly to a final, lightweight all-Aluminum design.
- Validated Performance: Conducted static structural and modal analyses, confirming stresses remained below yield strength and natural frequencies exceeded 80 Hz to avoid resonance.
- Delivered Results: Achieved a 27% weight reduction (from 33.25 kg to 27.58 kg) while maintaining a safety factor above 1.4.

Skills Demonstrated:
ANSYS (Static Structural, Modal Analysis), Design Iteration, Weight Optimization, Material Selection, Joint Definition.

Conclusion:
Successfully delivered a lighter, cost-effective, and structurally sound suspension design, demonstrating FEA’s practical application in automotive engineering.""",
        "images": ["chasis.jpg"],
        "pdf": "Suspension_Redesign.pdf"
    },
    {
        "id": 3,
        "title": "PCB Steady-State Thermal Optimization (Applied Heat Transfer Project)",
        "description": "Objective: To optimize the thermal management system of a printed circuit board (PCB) assembly, balancing cooling performance, weight, and cost.",
        "details": """Project Overview:
Performed steady-state thermal analysis on a multi-component PCB to ensure processor temperatures remained below 80°C. Evaluated different heat sink geometries and cooling configurations.

Key Actions & Results:
- Analyzed Configurations: Modeled three design iterations with varying heat sink types, thermal interface materials, and convective cooling settings.
- Optimized Trade-offs: Balanced performance metrics, identifying the most cost-effective solution that met all thermal and weight constraints.
- Provided Recommendation: Delivered a data-driven final recommendation that met the thermal goal at the lowest cost ($65).

Skills Demonstrated:
ANSYS Steady-State Thermal Analysis, Heat Sink Evaluation, Thermal Boundary Conditions, Cost/Performance Trade-off Analysis.

Conclusion:
This project showcased my ability to apply FEA to thermal challenges and make informed design decisions.""",
        "images": ["pcb1.jpg", "pcb2.jpg"],
        "pdf": "PCB_Thermal_Optimization.pdf"
    },
    {
        "id": 4,
        "title": "FEA Mesh Sensitivity & Correlation Study (Academic Project)",
        "description": "Objective: To systematically evaluate how mesh density and element type influence FEA accuracy for predicting stress concentrations.",
        "details": """Project Overview:
Conducted a mesh sensitivity study on a Titanium alloy plate with a central hole, creating multiple models with varying mesh densities (Coarse, Medium, Fine) and element types (4-node linear vs. 8-node quadratic).

Key Actions & Results:
- Systematic Comparison: Executed six simulation scenarios, comparing stress results against hand-calculated theoretical values.
- Quantified Accuracy: Achieved a correlation between FEA and theory, with fine 8-node mesh yielding 45,312 psi versus theoretical 45,250 psi (0.13% error).
- Developed Best Practices: Determined 8-node quadratic elements provide superior accuracy in high-stress areas.

Skills Demonstrated:
ANSYS Meshing Controls, Mesh Sensitivity Analysis, Element Type Selection, Theoretical Validation, Result Interpretation.

Conclusion:
Provided a foundation for FEA best practices, demonstrating ability to create reliable and validated simulation models.""",
        "images": ["1.jpg"],
        "pdf": "FEA_Mesh_Correlation.pdf"
    }
]

work_experiences = [
    {
        "title": "Molecular Diagnostics Mechanical Engineering Intern",
        "company": "Confidential Diagnostics Company",
        "period": "Jun 2023 – Dec 2025 (Present)",
        "location": "East Haven, CT",
        "description": """Developed and validated manufacturing processes for precision diagnostic components, integrating detailed technical reporting and process documentation to meet quality and regulatory standards.

• Collaborated with cross-functional teams and equipment vendors to refine machining, assembly, and testing procedures, applying root cause analysis to troubleshoot inefficiencies and support continuous improvement initiatives.
• Prepared comprehensive technical reports and process documentation summarizing test data and workflow enhancements to support design changes and process optimization.
• Conducted rigorous process validation and quality inspections to ensure compliance, leveraging CNC Machining knowledge and hands-on engagement to reinforce practical manufacturing safety protocols.
• Designed and fabricated heat block components for a patented laboratory device, optimizing thermal conductivity and precision fit.
• Developed CNC machining programs (G-code) and operated CNC mills and laser cutters to manufacture custom parts using aluminum and acrylic materials.""",
        "logo": "images/molecular.png",
    },
    {
        "title": "Teaching Assistant: Mechanical Engineering",
        "company": "University of New Haven",
        "period": "Jan 2025 – Present",
        "location": "West Haven, CT",
        "description": """Instructed undergraduate students on fundamental structural and thermal systems analysis, reinforcing mechanical engineering concepts essential for process understanding and design improvements.

• Conducted hands-on Mechanics and Instrumentation labs—including Tensile, Torsion, Stress Concentration, Thin Wall, Thermal, and Vibration analysis—to illustrate practical applications of technical reporting and process documentation.
• Supported faculty by grading, leading discussions, and guiding students in applying theoretical principles to practical experiments, fostering analytical thinking and problem-solving skills relevant to continuous improvement.""",
        "logo": "images/unh.png",
    }
]
