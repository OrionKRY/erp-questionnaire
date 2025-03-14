System Performance & Dependencies
=================================

.. tip::  
   This section evaluates the system’s availability, redundancy, performance metrics, and dependencies.

----

**System Availability & Uptime**
---------------------------------

.. note::  
   Understanding uptime requirements helps determine system reliability.

- **What is the system’s expected uptime?**  
  - ☐ 99.9% (High Availability)  
  - ☐ 99.5% (Standard)  
  - ☐ Below 99%  
- **Is there an established SLA (Service Level Agreement)?** (Yes/No)  
- **If yes, what are the recovery time objectives (RTO) and recovery point objectives (RPO)?**  

----

**Downtime & Failover Strategies**
----------------------------------

.. note::  
   Identifying downtime impact helps in planning disaster recovery.

- **What happens when this system is unavailable?**  
  - ☐ Work halts completely  
  - ☐ Degraded performance but operational  
  - ☐ Manual workarounds available  

- **Are there automatic failover mechanisms?** (Yes/No)  
- **If yes, describe failover method (e.g., redundant servers, cloud failover, etc.):**  
- **How is downtime communicated to users?**  
  - ☐ System notifications  
  - ☐ Email alerts  
  - ☐ Other: ______  

----

**System Dependencies**
-----------------------

.. note::  
   Dependencies impact system stability and performance.

- **Does this system rely on external services or APIs?** (Yes/No)  
- **List key dependent systems and their functions:**  

.. list-table::  
   :header-rows: 1  
   :widths: 40 60  

   * - **Dependent System**
     - **Dependency Type**
   * - Example: ERP Financials
     - Sends financial transactions
   * - Example: Authentication System
     - Provides user login authentication  
   * - 
     - 

----

**Performance Metrics**
-----------------------

.. note::  
   Tracking performance metrics ensures the system meets business needs.

- **What are the key performance indicators (KPIs) monitored?**  
  - ☐ Response time (ms)  
  - ☐ Transaction throughput  
  - ☐ Concurrent users  
  - ☐ CPU & memory utilization  
  - ☐ Other: ______  

- **Are system logs reviewed for performance analysis?** (Yes/No)  
- **Does the system undergo periodic load testing?** (Yes/No)  
- **If yes, what testing tools are used?**  
  - ☐ JMeter  
  - ☐ LoadRunner  
  - ☐ Other: ______  
