Verificando arquivos...
Código-fonte do programa: algoritmo.c
Arquivo de configuração de CPU: MyO3CPU.py --> MyO3CPU.py
Arquivo de configuração de caches e memória: MyCaches.py --> MyCaches.py
Arquivo de configuração de sistema: MySystem.py --> MySystem.py

**********************************************************************
* Compilando o programa ...
* gcc -static -o3 algoritmo.c -o algoritmo
**********************************************************************


**********************************************************************
* Executando o gem5...
* gem5 --outdir=m5out MySimulation.py -c algoritmo
**********************************************************************

gem5 Simulator System. http://gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 compiled Feb 16 2016 16:35:34
gem5 started Jul 6 2017 23:50:38
gem5 executing on simulacaolse3
command line: gem5 --outdir=m5out MySimulation.py -c algoritmo

Programa a ser executado: algoritmo
Global frequency set at 1000000000000 ticks per second
warn: DRAM device capacity (8192 Mbytes) does not match the address
range assigned (512 Mbytes)
0: system.remote_gdb.listener: listening for remote gdb on port 7000

---------------- Begin Simulation ----------------
info: Entering event queue @ 0. Starting simulation...

Finishing simulation. Current tick: 7570361000. Reason: target called
exit()
----------------- End Simulation -----------------
**********************************************************************
* Resultados da simulação
**********************************************************************

sim_seconds 0.007570 # Number of seconds simulated
sim_ticks 7570361000 # Number of ticks simulated
final_tick 7570361000 # Number of ticks from beginning of simulation
(restored from checkpoints and never reset)
sim_freq 1000000000000 # Frequency of simulated ticks
host_inst_rate 88430 # Simulator instruction rate (inst/s)
host_op_rate 164051 # Simulator op (including micro ops) rate (op/s)
host_tick_rate 96970008 # Simulator tick rate (ticks/s)
host_mem_usage 651292 # Number of bytes of host memory used
host_seconds 78.07 # Real time elapsed on the host
sim_insts 6903637 # Number of instructions simulated
sim_ops 12807285 # Number of ops (including micro ops) simulated
system.clk_domain.voltage_domain.voltage 1 # Voltage in Volts
system.clk_domain.clock 500 # Clock period in ticks
system.mem_ctrl.bytes_read::cpu.inst 14656 # Number of bytes read from
this memory
system.mem_ctrl.bytes_read::cpu.data 9344 # Number of bytes read from
this memory
system.mem_ctrl.bytes_read::total 24000 # Number of bytes read from this
memory
system.mem_ctrl.bytes_inst_read::cpu.inst 14656 # Number of instructions
bytes read from this memory
system.mem_ctrl.bytes_inst_read::total 14656 # Number of instructions
bytes read from this memory
system.mem_ctrl.num_reads::cpu.inst 229 # Number of read requests
responded to by this memory
system.mem_ctrl.num_reads::cpu.data 146 # Number of read requests
responded to by this memory
system.mem_ctrl.num_reads::total 375 # Number of read requests responded
to by this memory
system.mem_ctrl.bw_read::cpu.inst 1935971 # Total read bandwidth from
this memory (bytes/s)
system.mem_ctrl.bw_read::cpu.data 1234287 # Total read bandwidth from
this memory (bytes/s)
system.mem_ctrl.bw_read::total 3170258 # Total read bandwidth from this
memory (bytes/s)
system.mem_ctrl.bw_inst_read::cpu.inst 1935971 # Instruction read
bandwidth from this memory (bytes/s)
system.mem_ctrl.bw_inst_read::total 1935971 # Instruction read bandwidth
from this memory (bytes/s)
system.mem_ctrl.bw_total::cpu.inst 1935971 # Total bandwidth to/from
this memory (bytes/s)
system.mem_ctrl.bw_total::cpu.data 1234287 # Total bandwidth to/from
this memory (bytes/s)
system.mem_ctrl.bw_total::total 3170258 # Total bandwidth to/from this
memory (bytes/s)
system.mem_ctrl.readReqs 375 # Number of read requests accepted
system.mem_ctrl.writeReqs 0 # Number of write requests accepted
system.mem_ctrl.readBursts 375 # Number of DRAM read bursts, including
those serviced by the write queue
system.mem_ctrl.writeBursts 0 # Number of DRAM write bursts, including
those merged in the write queue
system.mem_ctrl.bytesReadDRAM 24000 # Total number of bytes read from DRAM
system.mem_ctrl.bytesReadWrQ 0 # Total number of bytes read from write
queue
system.mem_ctrl.bytesWritten 0 # Total number of bytes written to DRAM
system.mem_ctrl.bytesReadSys 24000 # Total read bytes from the system
interface side
system.mem_ctrl.bytesWrittenSys 0 # Total written bytes from the system
interface side
system.mem_ctrl.servicedByWrQ 0 # Number of DRAM read bursts serviced by
the write queue
system.mem_ctrl.mergedWrBursts 0 # Number of DRAM write bursts merged
with an existing one
system.mem_ctrl.neitherReadNorWriteReqs 0 # Number of requests that are
neither read nor write
system.mem_ctrl.perBankRdBursts::0 67 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::1 70 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::2 58 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::3 39 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::4 10 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::5 16 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::6 21 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::7 6 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::8 50 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::9 14 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::10 3 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::11 6 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::12 12 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::13 0 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::14 0 # Per bank write bursts
system.mem_ctrl.perBankRdBursts::15 3 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::0 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::1 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::2 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::3 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::4 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::5 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::6 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::7 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::8 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::9 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::10 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::11 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::12 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::13 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::14 0 # Per bank write bursts
system.mem_ctrl.perBankWrBursts::15 0 # Per bank write bursts
system.mem_ctrl.numRdRetry 0 # Number of times read queue was full
causing retry
system.mem_ctrl.numWrRetry 0 # Number of times write queue was full
causing retry
system.mem_ctrl.totGap 7570294000 # Total gap between requests
system.mem_ctrl.readPktSize::0 0 # Read request sizes (log2)
system.mem_ctrl.readPktSize::1 0 # Read request sizes (log2)
system.mem_ctrl.readPktSize::2 0 # Read request sizes (log2)
system.mem_ctrl.readPktSize::3 0 # Read request sizes (log2)
system.mem_ctrl.readPktSize::4 0 # Read request sizes (log2)
system.mem_ctrl.readPktSize::5 0 # Read request sizes (log2)
system.mem_ctrl.readPktSize::6 375 # Read request sizes (log2)
system.mem_ctrl.writePktSize::0 0 # Write request sizes (log2)
system.mem_ctrl.writePktSize::1 0 # Write request sizes (log2)
system.mem_ctrl.writePktSize::2 0 # Write request sizes (log2)
system.mem_ctrl.writePktSize::3 0 # Write request sizes (log2)
system.mem_ctrl.writePktSize::4 0 # Write request sizes (log2)
system.mem_ctrl.writePktSize::5 0 # Write request sizes (log2)
system.mem_ctrl.writePktSize::6 0 # Write request sizes (log2)
system.mem_ctrl.rdQLenPdf::0 249 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::1 100 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::2 20 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::3 6 # What read queue length does an incoming
req see
system.mem_ctrl.rdQLenPdf::4 0 # What read queue length does an incoming
req see
system.mem_ctrl.rdQLenPdf::5 0 # What read queue length does an incoming
req see
system.mem_ctrl.rdQLenPdf::6 0 # What read queue length does an incoming
req see
system.mem_ctrl.rdQLenPdf::7 0 # What read queue length does an incoming
req see
system.mem_ctrl.rdQLenPdf::8 0 # What read queue length does an incoming
req see
system.mem_ctrl.rdQLenPdf::9 0 # What read queue length does an incoming
req see
system.mem_ctrl.rdQLenPdf::10 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::11 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::12 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::13 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::14 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::15 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::16 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::17 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::18 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::19 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::20 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::21 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::22 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::23 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::24 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::25 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::26 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::27 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::28 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::29 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::30 0 # What read queue length does an
incoming req see
system.mem_ctrl.rdQLenPdf::31 0 # What read queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::0 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::1 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::2 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::3 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::4 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::5 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::6 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::7 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::8 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::9 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::10 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::11 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::12 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::13 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::14 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::15 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::16 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::17 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::18 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::19 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::20 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::21 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::22 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::23 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::24 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::25 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::26 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::27 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::28 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::29 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::30 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::31 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::32 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::33 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::34 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::35 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::36 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::37 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::38 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::39 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::40 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::41 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::42 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::43 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::44 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::45 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::46 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::47 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::48 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::49 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::50 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::51 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::52 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::53 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::54 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::55 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::56 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::57 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::58 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::59 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::60 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::61 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::62 0 # What write queue length does an
incoming req see
system.mem_ctrl.wrQLenPdf::63 0 # What write queue length does an
incoming req see
system.mem_ctrl.bytesPerActivate::samples 87 # Bytes accessed per row
activation
system.mem_ctrl.bytesPerActivate::mean 248.643678 # Bytes accessed per
row activation
system.mem_ctrl.bytesPerActivate::gmean 156.736101 # Bytes accessed per
row activation
system.mem_ctrl.bytesPerActivate::stdev 277.501728 # Bytes accessed per
row activation
system.mem_ctrl.bytesPerActivate::0-127 33 37.93% 37.93% # Bytes
accessed per row activation
system.mem_ctrl.bytesPerActivate::128-255 25 28.74% 66.67% # Bytes
accessed per row activation
system.mem_ctrl.bytesPerActivate::256-383 9 10.34% 77.01% # Bytes
accessed per row activation
system.mem_ctrl.bytesPerActivate::384-511 9 10.34% 87.36% # Bytes
accessed per row activation
system.mem_ctrl.bytesPerActivate::512-639 3 3.45% 90.80% # Bytes
accessed per row activation
system.mem_ctrl.bytesPerActivate::896-1023 2 2.30% 93.10% # Bytes
accessed per row activation
system.mem_ctrl.bytesPerActivate::1024-1151 6 6.90% 100.00% # Bytes
accessed per row activation
system.mem_ctrl.bytesPerActivate::total 87 # Bytes accessed per row
activation
system.mem_ctrl.totQLat 4178250 # Total ticks spent queuing
system.mem_ctrl.totMemAccLat 11209500 # Total ticks spent from burst
creation until serviced by the DRAM
system.mem_ctrl.totBusLat 1875000 # Total ticks spent in databus transfers
system.mem_ctrl.avgQLat 11142.00 # Average queueing delay per DRAM burst
system.mem_ctrl.avgBusLat 5000.00 # Average bus latency per DRAM burst
system.mem_ctrl.avgMemAccLat 29892.00 # Average memory access latency
per DRAM burst
system.mem_ctrl.avgRdBW 3.17 # Average DRAM read bandwidth in MiByte/s
system.mem_ctrl.avgWrBW 0.00 # Average achieved write bandwidth in MiByte/s
system.mem_ctrl.avgRdBWSys 3.17 # Average system read bandwidth in MiByte/s
system.mem_ctrl.avgWrBWSys 0.00 # Average system write bandwidth in
MiByte/s
system.mem_ctrl.peakBW 12800.00 # Theoretical peak bandwidth in MiByte/s
system.mem_ctrl.busUtil 0.02 # Data bus utilization in percentage
system.mem_ctrl.busUtilRead 0.02 # Data bus utilization in percentage
for reads
system.mem_ctrl.busUtilWrite 0.00 # Data bus utilization in percentage
for writes
system.mem_ctrl.avgRdQLen 1.00 # Average read queue length when enqueuing
system.mem_ctrl.avgWrQLen 0.00 # Average write queue length when enqueuing
system.mem_ctrl.readRowHits 280 # Number of row buffer hits during reads
system.mem_ctrl.writeRowHits 0 # Number of row buffer hits during writes
system.mem_ctrl.readRowHitRate 74.67 # Row buffer hit rate for reads
system.mem_ctrl.writeRowHitRate nan # Row buffer hit rate for writes
system.mem_ctrl.avgGap 20187450.67 # Average gap between requests
system.mem_ctrl.pageHitRate 74.67 # Row buffer hit rate, read and write
combined
system.mem_ctrl_0.actEnergy 461160 # Energy for activate commands per
rank (pJ)
system.mem_ctrl_0.preEnergy 251625 # Energy for precharge commands per
rank (pJ)
system.mem_ctrl_0.readEnergy 2004600 # Energy for read commands per rank
(pJ)
system.mem_ctrl_0.writeEnergy 0 # Energy for write commands per rank (pJ)
system.mem_ctrl_0.refreshEnergy 494320320 # Energy for refresh commands
per rank (pJ)
system.mem_ctrl_0.actBackEnergy 184783455 # Energy for active background
per rank (pJ)
system.mem_ctrl_0.preBackEnergy 4379026500 # Energy for precharge
background per rank (pJ)
system.mem_ctrl_0.totalEnergy 5060847660 # Total energy per rank (pJ)
system.mem_ctrl_0.averagePower 668.669939 # Core power per rank (mW)
system.mem_ctrl_0.memoryStateTime::IDLE 7284929250 # Time in different
power states
system.mem_ctrl_0.memoryStateTime::REF 252720000 # Time in different
power states
system.mem_ctrl_0.memoryStateTime::PRE_PDN 0 # Time in different power
states
system.mem_ctrl_0.memoryStateTime::ACT 30893000 # Time in different
power states
system.mem_ctrl_0.memoryStateTime::ACT_PDN 0 # Time in different power
states
system.mem_ctrl_1.actEnergy 196560 # Energy for activate commands per
rank (pJ)
system.mem_ctrl_1.preEnergy 107250 # Energy for precharge commands per
rank (pJ)
system.mem_ctrl_1.readEnergy 631800 # Energy for read commands per rank
(pJ)
system.mem_ctrl_1.writeEnergy 0 # Energy for write commands per rank (pJ)
system.mem_ctrl_1.refreshEnergy 494320320 # Energy for refresh commands
per rank (pJ)
system.mem_ctrl_1.actBackEnergy 182205630 # Energy for active background
per rank (pJ)
system.mem_ctrl_1.preBackEnergy 4381272000 # Energy for precharge
background per rank (pJ)
system.mem_ctrl_1.totalEnergy 5058733560 # Total energy per rank (pJ)
system.mem_ctrl_1.averagePower 668.392930 # Core power per rank (mW)
system.mem_ctrl_1.memoryStateTime::IDLE 7288786250 # Time in different
power states
system.mem_ctrl_1.memoryStateTime::REF 252720000 # Time in different
power states
system.mem_ctrl_1.memoryStateTime::PRE_PDN 0 # Time in different power
states
system.mem_ctrl_1.memoryStateTime::ACT 27138750 # Time in different
power states
system.mem_ctrl_1.memoryStateTime::ACT_PDN 0 # Time in different power
states
system.cpu.branchPred.lookups 301532 # Number of BP lookups
system.cpu.branchPred.condPredicted 301532 # Number of conditional
branches predicted
system.cpu.branchPred.condIncorrect 399 # Number of conditional branches
incorrect
system.cpu.branchPred.BTBLookups 301176 # Number of BTB lookups
system.cpu.branchPred.BTBHits 300389 # Number of BTB hits
system.cpu.branchPred.BTBCorrect 0 # Number of correct BTB predictions
(this stat may not work properly.
system.cpu.branchPred.BTBHitPct 99.738691 # BTB Hit Percentage
system.cpu.branchPred.usedRAS 132 # Number of times the RAS was used to
get a target.
system.cpu.branchPred.RASInCorrect 58 # Number of incorrect RAS
predictions.
system.cpu.apic_clk_domain.clock 8000 # Clock period in ticks
system.cpu.workload.num_syscalls 7 # Number of system calls
system.cpu.numCycles 15140723 # number of cpu cycles simulated
system.cpu.numWorkItemsStarted 0 # number of work items this cpu started
system.cpu.numWorkItemsCompleted 0 # number of work items this cpu
completed
system.cpu.fetch.icacheStallCycles 2112371 # Number of cycles fetch is
stalled on an Icache miss
system.cpu.fetch.Insts 6908523 # Number of instructions fetch has processed
system.cpu.fetch.Branches 301532 # Number of branches that fetch
encountered
system.cpu.fetch.predictedBranches 300521 # Number of branches that
fetch has predicted taken
system.cpu.fetch.Cycles 13010859 # Number of cycles fetch has run and
was not squashing or blocked
system.cpu.fetch.SquashCycles 1025 # Number of cycles fetch has spent
squashing
system.cpu.fetch.MiscStallCycles 25 # Number of cycles fetch has spent
waiting on interrupts, or bad addresses, or out of MSHRs
system.cpu.fetch.PendingTrapStallCycles 438 # Number of stall cycles due
to pending traps
system.cpu.fetch.PendingQuiesceStallCycles 13 # Number of stall cycles
due to pending quiesce instructions
system.cpu.fetch.CacheLines 2103063 # Number of cache lines fetched
system.cpu.fetch.IcacheSquashes 171 # Number of outstanding Icache
misses that were squashed
system.cpu.fetch.rateDist::samples 15124218 # Number of instructions
fetched each cycle (Total)
system.cpu.fetch.rateDist::mean 0.847438 # Number of instructions
fetched each cycle (Total)
system.cpu.fetch.rateDist::stdev 1.250991 # Number of instructions
fetched each cycle (Total)
system.cpu.fetch.rateDist::underflows 0 0.00% 0.00% # Number of
instructions fetched each cycle (Total)
system.cpu.fetch.rateDist::0 9867754 65.24% 65.24% # Number of
instructions fetched each cycle (Total)
system.cpu.fetch.rateDist::1 992568 6.56% 71.81% # Number of
instructions fetched each cycle (Total)
system.cpu.fetch.rateDist::2 967417 6.40% 78.20% # Number of
instructions fetched each cycle (Total)
system.cpu.fetch.rateDist::3 3296479 21.80% 100.00% # Number of
instructions fetched each cycle (Total)
system.cpu.fetch.rateDist::overflows 0 0.00% 100.00% # Number of
instructions fetched each cycle (Total)
system.cpu.fetch.rateDist::min_value 0 # Number of instructions fetched
each cycle (Total)
system.cpu.fetch.rateDist::max_value 3 # Number of instructions fetched
each cycle (Total)
system.cpu.fetch.rateDist::total 15124218 # Number of instructions
fetched each cycle (Total)
system.cpu.fetch.branchRate 0.019915 # Number of branch fetches per cycle
system.cpu.fetch.rate 0.456288 # Number of inst fetches per cycle
system.cpu.decode.IdleCycles 1712051 # Number of cycles decode is idle
system.cpu.decode.BlockedCycles 9139262 # Number of cycles decode is
blocked
system.cpu.decode.RunCycles 1572114 # Number of cycles decode is running
system.cpu.decode.UnblockCycles 2700279 # Number of cycles decode is
unblocking
system.cpu.decode.SquashCycles 512 # Number of cycles decode is squashing
system.cpu.decode.DecodedInsts 12814046 # Number of instructions handled
by decode
system.cpu.decode.SquashedInsts 1086 # Number of squashed instructions
handled by decode
system.cpu.rename.SquashCycles 512 # Number of cycles rename is squashing
system.cpu.rename.IdleCycles 3104399 # Number of cycles rename is idle
system.cpu.rename.BlockCycles 4927228 # Number of cycles rename is blocking
system.cpu.rename.serializeStallCycles 381 # count of cycles rename
stalled for serializing inst
system.cpu.rename.RunCycles 2463503 # Number of cycles rename is running
system.cpu.rename.UnblockCycles 4628195 # Number of cycles rename is
unblocking
system.cpu.rename.RenamedInsts 12812693 # Number of instructions
processed by rename
system.cpu.rename.SquashedInsts 553 # Number of squashed instructions
processed by rename
system.cpu.rename.ROBFullEvents 3241701 # Number of times rename has
blocked due to ROB full
system.cpu.rename.IQFullEvents 500154 # Number of times rename has
blocked due to IQ full
system.cpu.rename.SQFullEvents 3437 # Number of times rename has blocked
due to SQ full
system.cpu.rename.RenamedOperands 14213788 # Number of destination
operands rename has renamed
system.cpu.rename.RenameLookups 28230208 # Number of register rename
lookups that rename has made
system.cpu.rename.int_rename_lookups 15917584 # Number of integer rename
lookups
system.cpu.rename.fp_rename_lookups 4600911 # Number of floating rename
lookups
system.cpu.rename.CommittedMaps 14208077 # Number of HB maps that are
committed
system.cpu.rename.UndoneMaps 5711 # Number of HB maps that are undone
due to squashing
system.cpu.rename.serializingInsts 17 # count of serializing insts renamed
system.cpu.rename.tempSerializingInsts 17 # count of temporary
serializing insts renamed
system.cpu.rename.skidInsts 6916526 # count of insts added to the skid
buffer
system.cpu.memDep0.insertedLoads 2901445 # Number of loads inserted to
the mem dependence unit.
system.cpu.memDep0.insertedStores 1501152 # Number of stores inserted to
the mem dependence unit.
system.cpu.memDep0.conflictingLoads 2000042 # Number of conflicting loads.
system.cpu.memDep0.conflictingStores 1067167 # Number of conflicting
stores.
system.cpu.iq.iqInstsAdded 12812008 # Number of instructions added to
the IQ (excludes non-spec)
system.cpu.iq.iqNonSpecInstsAdded 31 # Number of non-speculative
instructions added to the IQ
system.cpu.iq.iqInstsIssued 12810613 # Number of instructions issued
system.cpu.iq.iqSquashedInstsIssued 172 # Number of squashed
instructions issued
system.cpu.iq.iqSquashedInstsExamined 4754 # Number of squashed
instructions iterated over during squash; mainly for profiling
system.cpu.iq.iqSquashedOperandsExamined 6004 # Number of squashed
operands that are examined and possibly removed from graph
system.cpu.iq.iqSquashedNonSpecRemoved 23 # Number of squashed non-spec
instructions that were removed
system.cpu.iq.issued_per_cycle::samples 15124218 # Number of insts
issued each cycle
system.cpu.iq.issued_per_cycle::mean 0.847026 # Number of insts issued
each cycle
system.cpu.iq.issued_per_cycle::stdev 0.770950 # Number of insts issued
each cycle
system.cpu.iq.issued_per_cycle::underflows 0 0.00% 0.00% # Number of
insts issued each cycle
system.cpu.iq.issued_per_cycle::0 5210561 34.45% 34.45% # Number of
insts issued each cycle
system.cpu.iq.issued_per_cycle::1 7567803 50.04% 84.49% # Number of
insts issued each cycle
system.cpu.iq.issued_per_cycle::2 1861497 12.31% 96.80% # Number of
insts issued each cycle
system.cpu.iq.issued_per_cycle::3 417612 2.76% 99.56% # Number of insts
issued each cycle
system.cpu.iq.issued_per_cycle::4 66745 0.44% 100.00% # Number of insts
issued each cycle
system.cpu.iq.issued_per_cycle::overflows 0 0.00% 100.00% # Number of
insts issued each cycle
system.cpu.iq.issued_per_cycle::min_value 0 # Number of insts issued
each cycle
system.cpu.iq.issued_per_cycle::max_value 4 # Number of insts issued
each cycle
system.cpu.iq.issued_per_cycle::total 15124218 # Number of insts issued
each cycle
system.cpu.iq.fu_full::No_OpClass 0 0.00% 0.00% # attempts to use FU
when none available
system.cpu.iq.fu_full::IntAlu 75999 10.71% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::IntMult 0 0.00% 10.71% # attempts to use FU when
none available
system.cpu.iq.fu_full::IntDiv 0 0.00% 10.71% # attempts to use FU when
none available
system.cpu.iq.fu_full::FloatAdd 24 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::FloatCmp 0 0.00% 10.71% # attempts to use FU when
none available
system.cpu.iq.fu_full::FloatCvt 0 0.00% 10.71% # attempts to use FU when
none available
system.cpu.iq.fu_full::FloatMult 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::FloatDiv 0 0.00% 10.71% # attempts to use FU when
none available
system.cpu.iq.fu_full::FloatSqrt 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::SimdAdd 0 0.00% 10.71% # attempts to use FU when
none available
system.cpu.iq.fu_full::SimdAddAcc 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::SimdAlu 0 0.00% 10.71% # attempts to use FU when
none available
system.cpu.iq.fu_full::SimdCmp 0 0.00% 10.71% # attempts to use FU when
none available
system.cpu.iq.fu_full::SimdCvt 0 0.00% 10.71% # attempts to use FU when
none available
system.cpu.iq.fu_full::SimdMisc 0 0.00% 10.71% # attempts to use FU when
none available
system.cpu.iq.fu_full::SimdMult 0 0.00% 10.71% # attempts to use FU when
none available
system.cpu.iq.fu_full::SimdMultAcc 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::SimdShift 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::SimdShiftAcc 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::SimdSqrt 0 0.00% 10.71% # attempts to use FU when
none available
system.cpu.iq.fu_full::SimdFloatAdd 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::SimdFloatAlu 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::SimdFloatCmp 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::SimdFloatCvt 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::SimdFloatDiv 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::SimdFloatMisc 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::SimdFloatMult 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::SimdFloatMultAcc 0 0.00% 10.71% # attempts to use
FU when none available
system.cpu.iq.fu_full::SimdFloatSqrt 0 0.00% 10.71% # attempts to use FU
when none available
system.cpu.iq.fu_full::MemRead 600121 84.56% 95.28% # attempts to use FU
when none available
system.cpu.iq.fu_full::MemWrite 33526 4.72% 100.00% # attempts to use FU
when none available
system.cpu.iq.fu_full::IprAccess 0 0.00% 100.00% # attempts to use FU
when none available
system.cpu.iq.fu_full::InstPrefetch 0 0.00% 100.00% # attempts to use FU
when none available
system.cpu.iq.FU_type_0::No_OpClass 122 0.00% 0.00% # Type of FU issued
system.cpu.iq.FU_type_0::IntAlu 5407924 42.21% 42.22% # Type of FU issued
system.cpu.iq.FU_type_0::IntMult 200014 1.56% 43.78% # Type of FU issued
system.cpu.iq.FU_type_0::IntDiv 14 0.00% 43.78% # Type of FU issued
system.cpu.iq.FU_type_0::FloatAdd 2800316 21.86% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::FloatCmp 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::FloatCvt 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::FloatMult 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::FloatDiv 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::FloatSqrt 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdAdd 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdAddAcc 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdAlu 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdCmp 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdCvt 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdMisc 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdMult 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdMultAcc 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdShift 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdShiftAcc 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdSqrt 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdFloatAdd 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdFloatAlu 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdFloatCmp 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdFloatCvt 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdFloatDiv 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdFloatMisc 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdFloatMult 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::SimdFloatMultAcc 0 0.00% 65.64% # Type of FU
issued
system.cpu.iq.FU_type_0::SimdFloatSqrt 0 0.00% 65.64% # Type of FU issued
system.cpu.iq.FU_type_0::MemRead 2901280 22.65% 88.28% # Type of FU issued
system.cpu.iq.FU_type_0::MemWrite 1500943 11.72% 100.00% # Type of FU
issued
system.cpu.iq.FU_type_0::IprAccess 0 0.00% 100.00% # Type of FU issued
system.cpu.iq.FU_type_0::InstPrefetch 0 0.00% 100.00% # Type of FU issued
system.cpu.iq.FU_type_0::total 12810613 # Type of FU issued
system.cpu.iq.rate 0.846103 # Inst issue rate
system.cpu.iq.fu_busy_cnt 709670 # FU busy when requested
system.cpu.iq.fu_busy_rate 0.055397 # FU busy rate (busy events/executed
inst)
system.cpu.iq.int_inst_queue_reads 29454093 # Number of integer
instruction queue reads
system.cpu.iq.int_inst_queue_writes 7015362 # Number of integer
instruction queue writes
system.cpu.iq.int_inst_queue_wakeup_accesses 7009311 # Number of integer
instruction queue wakeup accesses
system.cpu.iq.fp_inst_queue_reads 12001193 # Number of floating
instruction queue reads
system.cpu.iq.fp_inst_queue_writes 5801521 # Number of floating
instruction queue writes
system.cpu.iq.fp_inst_queue_wakeup_accesses 5800440 # Number of floating
instruction queue wakeup accesses
system.cpu.iq.int_alu_accesses 7319546 # Number of integer alu accesses
system.cpu.iq.fp_alu_accesses 6200615 # Number of floating point alu
accesses
system.cpu.iew.lsq.thread0.forwLoads 1599991 # Number of loads that had
data forwarded from stores
system.cpu.iew.lsq.thread0.invAddrLoads 0 # Number of loads ignored due
to an invalid address
system.cpu.iew.lsq.thread0.squashedLoads 801 # Number of loads squashed
system.cpu.iew.lsq.thread0.ignoredResponses 4 # Number of memory
responses ignored because the instruction is squashed
system.cpu.iew.lsq.thread0.memOrderViolation 90 # Number of memory
ordering violations
system.cpu.iew.lsq.thread0.squashedStores 428 # Number of stores squashed
system.cpu.iew.lsq.thread0.invAddrSwpfs 0 # Number of software
prefetches ignored due to an invalid address
system.cpu.iew.lsq.thread0.blockedLoads 0 # Number of blocked loads due
to partial load-store forwarding
system.cpu.iew.lsq.thread0.rescheduledLoads 0 # Number of loads that
were rescheduled
system.cpu.iew.lsq.thread0.cacheBlocked 14 # Number of times an access
to memory failed due to the cache being blocked
system.cpu.iew.iewIdleCycles 0 # Number of cycles IEW is idle
system.cpu.iew.iewSquashCycles 512 # Number of cycles IEW is squashing
system.cpu.iew.iewBlockCycles 300405 # Number of cycles IEW is blocking
system.cpu.iew.iewUnblockCycles 19 # Number of cycles IEW is unblocking
system.cpu.iew.iewDispatchedInsts 12812039 # Number of instructions
dispatched to IQ
system.cpu.iew.iewDispSquashedInsts 0 # Number of squashed instructions
skipped by dispatch
system.cpu.iew.iewDispLoadInsts 2901445 # Number of dispatched load
instructions
system.cpu.iew.iewDispStoreInsts 1501152 # Number of dispatched store
instructions
system.cpu.iew.iewDispNonSpecInsts 15 # Number of dispatched
non-speculative instructions
system.cpu.iew.iewIQFullEvents 1 # Number of times the IQ has become
full, causing a stall
system.cpu.iew.iewLSQFullEvents 16 # Number of times the LSQ has become
full, causing a stall
system.cpu.iew.memOrderViolationEvents 90 # Number of memory order
violations
system.cpu.iew.predictedTakenIncorrect 97 # Number of branches that were
predicted taken incorrectly
system.cpu.iew.predictedNotTakenIncorrect 347 # Number of branches that
were predicted not taken incorrectly
system.cpu.iew.branchMispredicts 444 # Number of branch mispredicts
detected at execute
system.cpu.iew.iewExecutedInsts 12809961 # Number of executed instructions
system.cpu.iew.iewExecLoadInsts 2901122 # Number of load instructions
executed
system.cpu.iew.iewExecSquashedInsts 652 # Number of squashed
instructions skipped in execute
system.cpu.iew.exec_swp 0 # number of swp insts executed
system.cpu.iew.exec_nop 0 # number of nop insts executed
system.cpu.iew.exec_refs 4401998 # number of memory reference insts
executed
system.cpu.iew.exec_branches 300912 # Number of branches executed
system.cpu.iew.exec_stores 1500876 # Number of stores executed
system.cpu.iew.exec_rate 0.846060 # Inst execution rate
system.cpu.iew.wb_sent 12809846 # cumulative count of insts sent to commit
system.cpu.iew.wb_count 12809751 # cumulative count of insts written-back
system.cpu.iew.wb_producers 7897651 # num instructions producing a value
system.cpu.iew.wb_consumers 12100287 # num instructions consuming a value
system.cpu.iew.wb_penalized 0 # number of instrctions required to write
to 'other' IQ
system.cpu.iew.wb_rate 0.846046 # insts written-back per cycle
system.cpu.iew.wb_fanout 0.652683 # average fanout of values written-back
system.cpu.iew.wb_penalized_rate 0 # fraction of instructions
written-back that wrote to 'other' IQ
system.cpu.commit.commitSquashedInsts 4076 # The number of squashed
insts skipped by commit
system.cpu.commit.commitNonSpecStalls 8 # The number of times commit has
been forced to stall to communicate backwards
system.cpu.commit.branchMispredicts 424 # The number of times a branch
was mispredicted
system.cpu.commit.committed_per_cycle::samples 15122908 # Number of
insts commited each cycle
system.cpu.commit.committed_per_cycle::mean 0.846880 # Number of insts
commited each cycle
system.cpu.commit.committed_per_cycle::stdev 1.177658 # Number of insts
commited each cycle
system.cpu.commit.committed_per_cycle::underflows 0 0.00% 0.00% # Number
of insts commited each cycle
system.cpu.commit.committed_per_cycle::0 8219530 54.35% 54.35% # Number
of insts commited each cycle
system.cpu.commit.committed_per_cycle::1 3701243 24.47% 78.83% # Number
of insts commited each cycle
system.cpu.commit.committed_per_cycle::2 1400968 9.26% 88.09% # Number
of insts commited each cycle
system.cpu.commit.committed_per_cycle::3 900562 5.95% 94.04% # Number of
insts commited each cycle
system.cpu.commit.committed_per_cycle::4 900605 5.96% 100.00% # Number
of insts commited each cycle
system.cpu.commit.committed_per_cycle::overflows 0 0.00% 100.00% #
Number of insts commited each cycle
system.cpu.commit.committed_per_cycle::min_value 0 # Number of insts
commited each cycle
system.cpu.commit.committed_per_cycle::max_value 4 # Number of insts
commited each cycle
system.cpu.commit.committed_per_cycle::total 15122908 # Number of insts
commited each cycle
system.cpu.commit.committedInsts 6903637 # Number of instructions committed
system.cpu.commit.committedOps 12807285 # Number of ops (including micro
ops) committed
system.cpu.commit.swp_count 0 # Number of s/w prefetches committed
system.cpu.commit.refs 4401368 # Number of memory references committed
system.cpu.commit.loads 2900644 # Number of loads committed
system.cpu.commit.membars 0 # Number of memory barriers committed
system.cpu.commit.branches 300796 # Number of branches committed
system.cpu.commit.fp_insts 5800147 # Number of committed floating point
instructions.
system.cpu.commit.int_insts 9607153 # Number of committed integer
instructions.
system.cpu.commit.function_calls 76 # Number of function calls committed.
system.cpu.commit.op_class_0::No_OpClass 43 0.00% 0.00% # Class of
committed instruction
system.cpu.commit.op_class_0::IntAlu 5405741 42.21% 42.21% # Class of
committed instruction
system.cpu.commit.op_class_0::IntMult 200005 1.56% 43.77% # Class of
committed instruction
system.cpu.commit.op_class_0::IntDiv 14 0.00% 43.77% # Class of
committed instruction
system.cpu.commit.op_class_0::FloatAdd 2800114 21.86% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::FloatCmp 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::FloatCvt 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::FloatMult 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::FloatDiv 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::FloatSqrt 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdAdd 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdAddAcc 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdAlu 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdCmp 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdCvt 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdMisc 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdMult 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdMultAcc 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdShift 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdShiftAcc 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdSqrt 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdFloatAdd 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdFloatAlu 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdFloatCmp 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdFloatCvt 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdFloatDiv 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdFloatMisc 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdFloatMult 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdFloatMultAcc 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::SimdFloatSqrt 0 0.00% 65.63% # Class of
committed instruction
system.cpu.commit.op_class_0::MemRead 2900644 22.65% 88.28% # Class of
committed instruction
system.cpu.commit.op_class_0::MemWrite 1500724 11.72% 100.00% # Class of
committed instruction
system.cpu.commit.op_class_0::IprAccess 0 0.00% 100.00% # Class of
committed instruction
system.cpu.commit.op_class_0::InstPrefetch 0 0.00% 100.00% # Class of
committed instruction
system.cpu.commit.op_class_0::total 12807285 # Class of committed
instruction
system.cpu.commit.bw_lim_events 900605 # number cycles where commit BW
limit reached
system.cpu.rob.rob_reads 27033664 # The number of ROB reads
system.cpu.rob.rob_writes 25624034 # The number of ROB writes
system.cpu.timesIdled 170 # Number of times that the entire CPU went
into an idle state and unscheduled itself
system.cpu.idleCycles 16505 # Total number of cycles that the CPU has
spent unscheduled due to idling
system.cpu.committedInsts 6903637 # Number of Instructions Simulated
system.cpu.committedOps 12807285 # Number of Ops (including micro ops)
Simulated
system.cpu.cpi 2.193152 # CPI: Cycles Per Instruction
system.cpu.cpi_total 2.193152 # CPI: Total CPI of All Threads
system.cpu.ipc 0.455965 # IPC: Instructions Per Cycle
system.cpu.ipc_total 0.455965 # IPC: Total IPC of All Threads
system.cpu.int_regfile_reads 15913276 # number of integer regfile reads
system.cpu.int_regfile_writes 6207537 # number of integer regfile writes
system.cpu.fp_regfile_reads 4600410 # number of floating regfile reads
system.cpu.fp_regfile_writes 5000407 # number of floating regfile writes
system.cpu.cc_regfile_reads 1904661 # number of cc regfile reads
system.cpu.cc_regfile_writes 3002821 # number of cc regfile writes
system.cpu.misc_regfile_reads 5804352 # number of misc regfile reads
system.cpu.misc_regfile_writes 1 # number of misc regfile writes
system.cpu.dcache.tags.replacements 1 # number of replacements
system.cpu.dcache.tags.tagsinuse 130.532665 # Cycle average of tags in use
system.cpu.dcache.tags.total_refs 2801628 # Total number of references
to valid blocks.
system.cpu.dcache.tags.sampled_refs 146 # Sample count of references to
valid blocks.
system.cpu.dcache.tags.avg_refs 19189.232877 # Average number of
references to valid blocks.
system.cpu.dcache.tags.warmup_cycle 0 # Cycle when the warmup percentage
was hit.
system.cpu.dcache.tags.occ_blocks::cpu.data 130.532665 # Average
occupied blocks per requestor
system.cpu.dcache.tags.occ_percent::cpu.data 0.254947 # Average
percentage of cache occupancy
system.cpu.dcache.tags.occ_percent::total 0.254947 # Average percentage
of cache occupancy
system.cpu.dcache.tags.occ_task_id_blocks::1024 145 # Occupied blocks
per task id
system.cpu.dcache.tags.age_task_id_blocks_1024::0 15 # Occupied blocks
per task id
system.cpu.dcache.tags.age_task_id_blocks_1024::3 130 # Occupied blocks
per task id
system.cpu.dcache.tags.occ_task_id_percent::1024 0.283203 # Percentage
of cache occupancy per task id
system.cpu.dcache.tags.tag_accesses 11207458 # Number of tag accesses
system.cpu.dcache.tags.data_accesses 11207458 # Number of data accesses
system.cpu.dcache.ReadReq_hits::cpu.data 1300979 # number of ReadReq hits
system.cpu.dcache.ReadReq_hits::total 1300979 # number of ReadReq hits
system.cpu.dcache.WriteReq_hits::cpu.data 1500649 # number of WriteReq hits
system.cpu.dcache.WriteReq_hits::total 1500649 # number of WriteReq hits
system.cpu.dcache.demand_hits::cpu.data 2801628 # number of demand
(read+write) hits
system.cpu.dcache.demand_hits::total 2801628 # number of demand
(read+write) hits
system.cpu.dcache.overall_hits::cpu.data 2801628 # number of overall hits
system.cpu.dcache.overall_hits::total 2801628 # number of overall hits
system.cpu.dcache.ReadReq_misses::cpu.data 125 # number of ReadReq misses
system.cpu.dcache.ReadReq_misses::total 125 # number of ReadReq misses
system.cpu.dcache.WriteReq_misses::cpu.data 75 # number of WriteReq misses
system.cpu.dcache.WriteReq_misses::total 75 # number of WriteReq misses
system.cpu.dcache.demand_misses::cpu.data 200 # number of demand
(read+write) misses
system.cpu.dcache.demand_misses::total 200 # number of demand
(read+write) misses
system.cpu.dcache.overall_misses::cpu.data 200 # number of overall misses
system.cpu.dcache.overall_misses::total 200 # number of overall misses
system.cpu.dcache.ReadReq_miss_latency::cpu.data 8574500 # number of
ReadReq miss cycles
system.cpu.dcache.ReadReq_miss_latency::total 8574500 # number of
ReadReq miss cycles
system.cpu.dcache.WriteReq_miss_latency::cpu.data 4993250 # number of
WriteReq miss cycles
system.cpu.dcache.WriteReq_miss_latency::total 4993250 # number of
WriteReq miss cycles
system.cpu.dcache.demand_miss_latency::cpu.data 13567750 # number of
demand (read+write) miss cycles
system.cpu.dcache.demand_miss_latency::total 13567750 # number of demand
(read+write) miss cycles
system.cpu.dcache.overall_miss_latency::cpu.data 13567750 # number of
overall miss cycles
system.cpu.dcache.overall_miss_latency::total 13567750 # number of
overall miss cycles
system.cpu.dcache.ReadReq_accesses::cpu.data 1301104 # number of ReadReq
accesses(hits+misses)
system.cpu.dcache.ReadReq_accesses::total 1301104 # number of ReadReq
accesses(hits+misses)
system.cpu.dcache.WriteReq_accesses::cpu.data 1500724 # number of
WriteReq accesses(hits+misses)
system.cpu.dcache.WriteReq_accesses::total 1500724 # number of WriteReq
accesses(hits+misses)
system.cpu.dcache.demand_accesses::cpu.data 2801828 # number of demand
(read+write) accesses
system.cpu.dcache.demand_accesses::total 2801828 # number of demand
(read+write) accesses
system.cpu.dcache.overall_accesses::cpu.data 2801828 # number of overall
(read+write) accesses
system.cpu.dcache.overall_accesses::total 2801828 # number of overall
(read+write) accesses
system.cpu.dcache.ReadReq_miss_rate::cpu.data 0.000096 # miss rate for
ReadReq accesses
system.cpu.dcache.ReadReq_miss_rate::total 0.000096 # miss rate for
ReadReq accesses
system.cpu.dcache.WriteReq_miss_rate::cpu.data 0.000050 # miss rate for
WriteReq accesses
system.cpu.dcache.WriteReq_miss_rate::total 0.000050 # miss rate for
WriteReq accesses
system.cpu.dcache.demand_miss_rate::cpu.data 0.000071 # miss rate for
demand accesses
system.cpu.dcache.demand_miss_rate::total 0.000071 # miss rate for
demand accesses
system.cpu.dcache.overall_miss_rate::cpu.data 0.000071 # miss rate for
overall accesses
system.cpu.dcache.overall_miss_rate::total 0.000071 # miss rate for
overall accesses
system.cpu.dcache.ReadReq_avg_miss_latency::cpu.data 68596 # average
ReadReq miss latency
system.cpu.dcache.ReadReq_avg_miss_latency::total 68596 # average
ReadReq miss latency
system.cpu.dcache.WriteReq_avg_miss_latency::cpu.data 66576.666667 #
average WriteReq miss latency
system.cpu.dcache.WriteReq_avg_miss_latency::total 66576.666667 #
average WriteReq miss latency
system.cpu.dcache.demand_avg_miss_latency::cpu.data 67838.750000 #
average overall miss latency
system.cpu.dcache.demand_avg_miss_latency::total 67838.750000 # average
overall miss latency
system.cpu.dcache.overall_avg_miss_latency::cpu.data 67838.750000 #
average overall miss latency
system.cpu.dcache.overall_avg_miss_latency::total 67838.750000 # average
overall miss latency
system.cpu.dcache.blocked_cycles::no_mshrs 265 # number of cycles access
was blocked
system.cpu.dcache.blocked_cycles::no_targets 0 # number of cycles access
was blocked
system.cpu.dcache.blocked::no_mshrs 6 # number of cycles access was blocked
system.cpu.dcache.blocked::no_targets 0 # number of cycles access was
blocked
system.cpu.dcache.avg_blocked_cycles::no_mshrs 44.166667 # average
number of cycles each access was blocked
system.cpu.dcache.avg_blocked_cycles::no_targets nan # average number of
cycles each access was blocked
system.cpu.dcache.fast_writes 0 # number of fast writes performed
system.cpu.dcache.cache_copies 0 # number of cache copies performed
system.cpu.dcache.writebacks::writebacks 1 # number of writebacks
system.cpu.dcache.writebacks::total 1 # number of writebacks
system.cpu.dcache.ReadReq_mshr_hits::cpu.data 54 # number of ReadReq
MSHR hits
system.cpu.dcache.ReadReq_mshr_hits::total 54 # number of ReadReq MSHR hits
system.cpu.dcache.demand_mshr_hits::cpu.data 54 # number of demand
(read+write) MSHR hits
system.cpu.dcache.demand_mshr_hits::total 54 # number of demand
(read+write) MSHR hits
system.cpu.dcache.overall_mshr_hits::cpu.data 54 # number of overall
MSHR hits
system.cpu.dcache.overall_mshr_hits::total 54 # number of overall MSHR hits
system.cpu.dcache.ReadReq_mshr_misses::cpu.data 71 # number of ReadReq
MSHR misses
system.cpu.dcache.ReadReq_mshr_misses::total 71 # number of ReadReq MSHR
misses
system.cpu.dcache.WriteReq_mshr_misses::cpu.data 75 # number of WriteReq
MSHR misses
system.cpu.dcache.WriteReq_mshr_misses::total 75 # number of WriteReq
MSHR misses
system.cpu.dcache.demand_mshr_misses::cpu.data 146 # number of demand
(read+write) MSHR misses
system.cpu.dcache.demand_mshr_misses::total 146 # number of demand
(read+write) MSHR misses
system.cpu.dcache.overall_mshr_misses::cpu.data 146 # number of overall
MSHR misses
system.cpu.dcache.overall_mshr_misses::total 146 # number of overall
MSHR misses
system.cpu.dcache.ReadReq_mshr_miss_latency::cpu.data 5166750 # number
of ReadReq MSHR miss cycles
system.cpu.dcache.ReadReq_mshr_miss_latency::total 5166750 # number of
ReadReq MSHR miss cycles
system.cpu.dcache.WriteReq_mshr_miss_latency::cpu.data 4811750 # number
of WriteReq MSHR miss cycles
system.cpu.dcache.WriteReq_mshr_miss_latency::total 4811750 # number of
WriteReq MSHR miss cycles
system.cpu.dcache.demand_mshr_miss_latency::cpu.data 9978500 # number of
demand (read+write) MSHR miss cycles
system.cpu.dcache.demand_mshr_miss_latency::total 9978500 # number of
demand (read+write) MSHR miss cycles
system.cpu.dcache.overall_mshr_miss_latency::cpu.data 9978500 # number
of overall MSHR miss cycles
system.cpu.dcache.overall_mshr_miss_latency::total 9978500 # number of
overall MSHR miss cycles
system.cpu.dcache.ReadReq_mshr_miss_rate::cpu.data 0.000055 # mshr miss
rate for ReadReq accesses
system.cpu.dcache.ReadReq_mshr_miss_rate::total 0.000055 # mshr miss
rate for ReadReq accesses
system.cpu.dcache.WriteReq_mshr_miss_rate::cpu.data 0.000050 # mshr miss
rate for WriteReq accesses
system.cpu.dcache.WriteReq_mshr_miss_rate::total 0.000050 # mshr miss
rate for WriteReq accesses
system.cpu.dcache.demand_mshr_miss_rate::cpu.data 0.000052 # mshr miss
rate for demand accesses
system.cpu.dcache.demand_mshr_miss_rate::total 0.000052 # mshr miss rate
for demand accesses
system.cpu.dcache.overall_mshr_miss_rate::cpu.data 0.000052 # mshr miss
rate for overall accesses
system.cpu.dcache.overall_mshr_miss_rate::total 0.000052 # mshr miss
rate for overall accesses
system.cpu.dcache.ReadReq_avg_mshr_miss_latency::cpu.data 72771.126761 #
average ReadReq mshr miss latency
system.cpu.dcache.ReadReq_avg_mshr_miss_latency::total 72771.126761 #
average ReadReq mshr miss latency
system.cpu.dcache.WriteReq_avg_mshr_miss_latency::cpu.data 64156.666667
# average WriteReq mshr miss latency
system.cpu.dcache.WriteReq_avg_mshr_miss_latency::total 64156.666667 #
average WriteReq mshr miss latency
system.cpu.dcache.demand_avg_mshr_miss_latency::cpu.data 68345.890411 #
average overall mshr miss latency
system.cpu.dcache.demand_avg_mshr_miss_latency::total 68345.890411 #
average overall mshr miss latency
system.cpu.dcache.overall_avg_mshr_miss_latency::cpu.data 68345.890411 #
average overall mshr miss latency
system.cpu.dcache.overall_avg_mshr_miss_latency::total 68345.890411 #
average overall mshr miss latency
system.cpu.dcache.no_allocate_misses 0 # Number of misses that were
no-allocate
system.cpu.icache.tags.replacements 6 # number of replacements
system.cpu.icache.tags.tagsinuse 194.483787 # Cycle average of tags in use
system.cpu.icache.tags.total_refs 2102780 # Total number of references
to valid blocks.
system.cpu.icache.tags.sampled_refs 230 # Sample count of references to
valid blocks.
system.cpu.icache.tags.avg_refs 9142.521739 # Average number of
references to valid blocks.
system.cpu.icache.tags.warmup_cycle 0 # Cycle when the warmup percentage
was hit.
system.cpu.icache.tags.occ_blocks::cpu.inst 194.483787 # Average
occupied blocks per requestor
system.cpu.icache.tags.occ_percent::cpu.inst 0.379851 # Average
percentage of cache occupancy
system.cpu.icache.tags.occ_percent::total 0.379851 # Average percentage
of cache occupancy
system.cpu.icache.tags.occ_task_id_blocks::1024 224 # Occupied blocks
per task id
system.cpu.icache.tags.age_task_id_blocks_1024::0 31 # Occupied blocks
per task id
system.cpu.icache.tags.age_task_id_blocks_1024::3 193 # Occupied blocks
per task id
system.cpu.icache.tags.occ_task_id_percent::1024 0.437500 # Percentage
of cache occupancy per task id
system.cpu.icache.tags.tag_accesses 8412482 # Number of tag accesses
system.cpu.icache.tags.data_accesses 8412482 # Number of data accesses
system.cpu.icache.ReadReq_hits::cpu.inst 2102780 # number of ReadReq hits
system.cpu.icache.ReadReq_hits::total 2102780 # number of ReadReq hits
system.cpu.icache.demand_hits::cpu.inst 2102780 # number of demand
(read+write) hits
system.cpu.icache.demand_hits::total 2102780 # number of demand
(read+write) hits
system.cpu.icache.overall_hits::cpu.inst 2102780 # number of overall hits
system.cpu.icache.overall_hits::total 2102780 # number of overall hits
system.cpu.icache.ReadReq_misses::cpu.inst 283 # number of ReadReq misses
system.cpu.icache.ReadReq_misses::total 283 # number of ReadReq misses
system.cpu.icache.demand_misses::cpu.inst 283 # number of demand
(read+write) misses
system.cpu.icache.demand_misses::total 283 # number of demand
(read+write) misses
system.cpu.icache.overall_misses::cpu.inst 283 # number of overall misses
system.cpu.icache.overall_misses::total 283 # number of overall misses
system.cpu.icache.ReadReq_miss_latency::cpu.inst 19768750 # number of
ReadReq miss cycles
system.cpu.icache.ReadReq_miss_latency::total 19768750 # number of
ReadReq miss cycles
system.cpu.icache.demand_miss_latency::cpu.inst 19768750 # number of
demand (read+write) miss cycles
system.cpu.icache.demand_miss_latency::total 19768750 # number of demand
(read+write) miss cycles
system.cpu.icache.overall_miss_latency::cpu.inst 19768750 # number of
overall miss cycles
system.cpu.icache.overall_miss_latency::total 19768750 # number of
overall miss cycles
system.cpu.icache.ReadReq_accesses::cpu.inst 2103063 # number of ReadReq
accesses(hits+misses)
system.cpu.icache.ReadReq_accesses::total 2103063 # number of ReadReq
accesses(hits+misses)
system.cpu.icache.demand_accesses::cpu.inst 2103063 # number of demand
(read+write) accesses
system.cpu.icache.demand_accesses::total 2103063 # number of demand
(read+write) accesses
system.cpu.icache.overall_accesses::cpu.inst 2103063 # number of overall
(read+write) accesses
system.cpu.icache.overall_accesses::total 2103063 # number of overall
(read+write) accesses
system.cpu.icache.ReadReq_miss_rate::cpu.inst 0.000135 # miss rate for
ReadReq accesses
system.cpu.icache.ReadReq_miss_rate::total 0.000135 # miss rate for
ReadReq accesses
system.cpu.icache.demand_miss_rate::cpu.inst 0.000135 # miss rate for
demand accesses
system.cpu.icache.demand_miss_rate::total 0.000135 # miss rate for
demand accesses
system.cpu.icache.overall_miss_rate::cpu.inst 0.000135 # miss rate for
overall accesses
system.cpu.icache.overall_miss_rate::total 0.000135 # miss rate for
overall accesses
system.cpu.icache.ReadReq_avg_miss_latency::cpu.inst 69854.240283 #
average ReadReq miss latency
system.cpu.icache.ReadReq_avg_miss_latency::total 69854.240283 # average
ReadReq miss latency
system.cpu.icache.demand_avg_miss_latency::cpu.inst 69854.240283 #
average overall miss latency
system.cpu.icache.demand_avg_miss_latency::total 69854.240283 # average
overall miss latency
system.cpu.icache.overall_avg_miss_latency::cpu.inst 69854.240283 #
average overall miss latency
system.cpu.icache.overall_avg_miss_latency::total 69854.240283 # average
overall miss latency
system.cpu.icache.blocked_cycles::no_mshrs 0 # number of cycles access
was blocked
system.cpu.icache.blocked_cycles::no_targets 0 # number of cycles access
was blocked
system.cpu.icache.blocked::no_mshrs 0 # number of cycles access was blocked
system.cpu.icache.blocked::no_targets 0 # number of cycles access was
blocked
system.cpu.icache.avg_blocked_cycles::no_mshrs nan # average number of
cycles each access was blocked
system.cpu.icache.avg_blocked_cycles::no_targets nan # average number of
cycles each access was blocked
system.cpu.icache.fast_writes 0 # number of fast writes performed
system.cpu.icache.cache_copies 0 # number of cache copies performed
system.cpu.icache.ReadReq_mshr_hits::cpu.inst 53 # number of ReadReq
MSHR hits
system.cpu.icache.ReadReq_mshr_hits::total 53 # number of ReadReq MSHR hits
system.cpu.icache.demand_mshr_hits::cpu.inst 53 # number of demand
(read+write) MSHR hits
system.cpu.icache.demand_mshr_hits::total 53 # number of demand
(read+write) MSHR hits
system.cpu.icache.overall_mshr_hits::cpu.inst 53 # number of overall
MSHR hits
system.cpu.icache.overall_mshr_hits::total 53 # number of overall MSHR hits
system.cpu.icache.ReadReq_mshr_misses::cpu.inst 230 # number of ReadReq
MSHR misses
system.cpu.icache.ReadReq_mshr_misses::total 230 # number of ReadReq
MSHR misses
system.cpu.icache.demand_mshr_misses::cpu.inst 230 # number of demand
(read+write) MSHR misses
system.cpu.icache.demand_mshr_misses::total 230 # number of demand
(read+write) MSHR misses
system.cpu.icache.overall_mshr_misses::cpu.inst 230 # number of overall
MSHR misses
system.cpu.icache.overall_mshr_misses::total 230 # number of overall
MSHR misses
system.cpu.icache.ReadReq_mshr_miss_latency::cpu.inst 16026000 # number
of ReadReq MSHR miss cycles
system.cpu.icache.ReadReq_mshr_miss_latency::total 16026000 # number of
ReadReq MSHR miss cycles
system.cpu.icache.demand_mshr_miss_latency::cpu.inst 16026000 # number
of demand (read+write) MSHR miss cycles
system.cpu.icache.demand_mshr_miss_latency::total 16026000 # number of
demand (read+write) MSHR miss cycles
system.cpu.icache.overall_mshr_miss_latency::cpu.inst 16026000 # number
of overall MSHR miss cycles
system.cpu.icache.overall_mshr_miss_latency::total 16026000 # number of
overall MSHR miss cycles
system.cpu.icache.ReadReq_mshr_miss_rate::cpu.inst 0.000109 # mshr miss
rate for ReadReq accesses
system.cpu.icache.ReadReq_mshr_miss_rate::total 0.000109 # mshr miss
rate for ReadReq accesses
system.cpu.icache.demand_mshr_miss_rate::cpu.inst 0.000109 # mshr miss
rate for demand accesses
system.cpu.icache.demand_mshr_miss_rate::total 0.000109 # mshr miss rate
for demand accesses
system.cpu.icache.overall_mshr_miss_rate::cpu.inst 0.000109 # mshr miss
rate for overall accesses
system.cpu.icache.overall_mshr_miss_rate::total 0.000109 # mshr miss
rate for overall accesses
system.cpu.icache.ReadReq_avg_mshr_miss_latency::cpu.inst 69678.260870 #
average ReadReq mshr miss latency
system.cpu.icache.ReadReq_avg_mshr_miss_latency::total 69678.260870 #
average ReadReq mshr miss latency
system.cpu.icache.demand_avg_mshr_miss_latency::cpu.inst 69678.260870 #
average overall mshr miss latency
system.cpu.icache.demand_avg_mshr_miss_latency::total 69678.260870 #
average overall mshr miss latency
system.cpu.icache.overall_avg_mshr_miss_latency::cpu.inst 69678.260870 #
average overall mshr miss latency
system.cpu.icache.overall_avg_mshr_miss_latency::total 69678.260870 #
average overall mshr miss latency
system.cpu.icache.no_allocate_misses 0 # Number of misses that were
no-allocate
system.cpu.l2cache.tags.replacements 0 # number of replacements
system.cpu.l2cache.tags.tagsinuse 253.100774 # Cycle average of tags in use
system.cpu.l2cache.tags.total_refs 2 # Total number of references to
valid blocks.
system.cpu.l2cache.tags.sampled_refs 300 # Sample count of references to
valid blocks.
system.cpu.l2cache.tags.avg_refs 0.006667 # Average number of references
to valid blocks.
system.cpu.l2cache.tags.warmup_cycle 0 # Cycle when the warmup
percentage was hit.
system.cpu.l2cache.tags.occ_blocks::cpu.inst 196.480412 # Average
occupied blocks per requestor
system.cpu.l2cache.tags.occ_blocks::cpu.data 56.620362 # Average
occupied blocks per requestor
system.cpu.l2cache.tags.occ_percent::cpu.inst 0.002998 # Average
percentage of cache occupancy
system.cpu.l2cache.tags.occ_percent::cpu.data 0.000864 # Average
percentage of cache occupancy
system.cpu.l2cache.tags.occ_percent::total 0.003862 # Average percentage
of cache occupancy
system.cpu.l2cache.tags.occ_task_id_blocks::1024 300 # Occupied blocks
per task id
system.cpu.l2cache.tags.age_task_id_blocks_1024::0 45 # Occupied blocks
per task id
system.cpu.l2cache.tags.age_task_id_blocks_1024::3 255 # Occupied blocks
per task id
system.cpu.l2cache.tags.occ_task_id_percent::1024 0.004578 # Percentage
of cache occupancy per task id
system.cpu.l2cache.tags.tag_accesses 3391 # Number of tag accesses
system.cpu.l2cache.tags.data_accesses 3391 # Number of data accesses
system.cpu.l2cache.ReadReq_hits::cpu.inst 1 # number of ReadReq hits
system.cpu.l2cache.ReadReq_hits::total 1 # number of ReadReq hits
system.cpu.l2cache.Writeback_hits::writebacks 1 # number of Writeback hits
system.cpu.l2cache.Writeback_hits::total 1 # number of Writeback hits
system.cpu.l2cache.demand_hits::cpu.inst 1 # number of demand
(read+write) hits
system.cpu.l2cache.demand_hits::total 1 # number of demand (read+write)
hits
system.cpu.l2cache.overall_hits::cpu.inst 1 # number of overall hits
system.cpu.l2cache.overall_hits::total 1 # number of overall hits
system.cpu.l2cache.ReadReq_misses::cpu.inst 229 # number of ReadReq misses
system.cpu.l2cache.ReadReq_misses::cpu.data 71 # number of ReadReq misses
system.cpu.l2cache.ReadReq_misses::total 300 # number of ReadReq misses
system.cpu.l2cache.ReadExReq_misses::cpu.data 75 # number of ReadExReq
misses
system.cpu.l2cache.ReadExReq_misses::total 75 # number of ReadExReq misses
system.cpu.l2cache.demand_misses::cpu.inst 229 # number of demand
(read+write) misses
system.cpu.l2cache.demand_misses::cpu.data 146 # number of demand
(read+write) misses
system.cpu.l2cache.demand_misses::total 375 # number of demand
(read+write) misses
system.cpu.l2cache.overall_misses::cpu.inst 229 # number of overall misses
system.cpu.l2cache.overall_misses::cpu.data 146 # number of overall misses
system.cpu.l2cache.overall_misses::total 375 # number of overall misses
system.cpu.l2cache.ReadReq_miss_latency::cpu.inst 15788000 # number of
ReadReq miss cycles
system.cpu.l2cache.ReadReq_miss_latency::cpu.data 5095750 # number of
ReadReq miss cycles
system.cpu.l2cache.ReadReq_miss_latency::total 20883750 # number of
ReadReq miss cycles
system.cpu.l2cache.ReadExReq_miss_latency::cpu.data 4736750 # number of
ReadExReq miss cycles
system.cpu.l2cache.ReadExReq_miss_latency::total 4736750 # number of
ReadExReq miss cycles
system.cpu.l2cache.demand_miss_latency::cpu.inst 15788000 # number of
demand (read+write) miss cycles
system.cpu.l2cache.demand_miss_latency::cpu.data 9832500 # number of
demand (read+write) miss cycles
system.cpu.l2cache.demand_miss_latency::total 25620500 # number of
demand (read+write) miss cycles
system.cpu.l2cache.overall_miss_latency::cpu.inst 15788000 # number of
overall miss cycles
system.cpu.l2cache.overall_miss_latency::cpu.data 9832500 # number of
overall miss cycles
system.cpu.l2cache.overall_miss_latency::total 25620500 # number of
overall miss cycles
system.cpu.l2cache.ReadReq_accesses::cpu.inst 230 # number of ReadReq
accesses(hits+misses)
system.cpu.l2cache.ReadReq_accesses::cpu.data 71 # number of ReadReq
accesses(hits+misses)
system.cpu.l2cache.ReadReq_accesses::total 301 # number of ReadReq
accesses(hits+misses)
system.cpu.l2cache.Writeback_accesses::writebacks 1 # number of
Writeback accesses(hits+misses)
system.cpu.l2cache.Writeback_accesses::total 1 # number of Writeback
accesses(hits+misses)
system.cpu.l2cache.ReadExReq_accesses::cpu.data 75 # number of ReadExReq
accesses(hits+misses)
system.cpu.l2cache.ReadExReq_accesses::total 75 # number of ReadExReq
accesses(hits+misses)
system.cpu.l2cache.demand_accesses::cpu.inst 230 # number of demand
(read+write) accesses
system.cpu.l2cache.demand_accesses::cpu.data 146 # number of demand
(read+write) accesses
system.cpu.l2cache.demand_accesses::total 376 # number of demand
(read+write) accesses
system.cpu.l2cache.overall_accesses::cpu.inst 230 # number of overall
(read+write) accesses
system.cpu.l2cache.overall_accesses::cpu.data 146 # number of overall
(read+write) accesses
system.cpu.l2cache.overall_accesses::total 376 # number of overall
(read+write) accesses
system.cpu.l2cache.ReadReq_miss_rate::cpu.inst 0.995652 # miss rate for
ReadReq accesses
system.cpu.l2cache.ReadReq_miss_rate::cpu.data 1 # miss rate for ReadReq
accesses
system.cpu.l2cache.ReadReq_miss_rate::total 0.996678 # miss rate for
ReadReq accesses
system.cpu.l2cache.ReadExReq_miss_rate::cpu.data 1 # miss rate for
ReadExReq accesses
system.cpu.l2cache.ReadExReq_miss_rate::total 1 # miss rate for
ReadExReq accesses
system.cpu.l2cache.demand_miss_rate::cpu.inst 0.995652 # miss rate for
demand accesses
system.cpu.l2cache.demand_miss_rate::cpu.data 1 # miss rate for demand
accesses
system.cpu.l2cache.demand_miss_rate::total 0.997340 # miss rate for
demand accesses
system.cpu.l2cache.overall_miss_rate::cpu.inst 0.995652 # miss rate for
overall accesses
system.cpu.l2cache.overall_miss_rate::cpu.data 1 # miss rate for overall
accesses
system.cpu.l2cache.overall_miss_rate::total 0.997340 # miss rate for
overall accesses
system.cpu.l2cache.ReadReq_avg_miss_latency::cpu.inst 68943.231441 #
average ReadReq miss latency
system.cpu.l2cache.ReadReq_avg_miss_latency::cpu.data 71771.126761 #
average ReadReq miss latency
system.cpu.l2cache.ReadReq_avg_miss_latency::total 69612.500000 #
average ReadReq miss latency
system.cpu.l2cache.ReadExReq_avg_miss_latency::cpu.data 63156.666667 #
average ReadExReq miss latency
system.cpu.l2cache.ReadExReq_avg_miss_latency::total 63156.666667 #
average ReadExReq miss latency
system.cpu.l2cache.demand_avg_miss_latency::cpu.inst 68943.231441 #
average overall miss latency
system.cpu.l2cache.demand_avg_miss_latency::cpu.data 67345.890411 #
average overall miss latency
system.cpu.l2cache.demand_avg_miss_latency::total 68321.333333 # average
overall miss latency
system.cpu.l2cache.overall_avg_miss_latency::cpu.inst 68943.231441 #
average overall miss latency
system.cpu.l2cache.overall_avg_miss_latency::cpu.data 67345.890411 #
average overall miss latency
system.cpu.l2cache.overall_avg_miss_latency::total 68321.333333 #
average overall miss latency
system.cpu.l2cache.blocked_cycles::no_mshrs 0 # number of cycles access
was blocked
system.cpu.l2cache.blocked_cycles::no_targets 0 # number of cycles
access was blocked
system.cpu.l2cache.blocked::no_mshrs 0 # number of cycles access was
blocked
system.cpu.l2cache.blocked::no_targets 0 # number of cycles access was
blocked
system.cpu.l2cache.avg_blocked_cycles::no_mshrs nan # average number of
cycles each access was blocked
system.cpu.l2cache.avg_blocked_cycles::no_targets nan # average number
of cycles each access was blocked
system.cpu.l2cache.fast_writes 0 # number of fast writes performed
system.cpu.l2cache.cache_copies 0 # number of cache copies performed
system.cpu.l2cache.ReadReq_mshr_misses::cpu.inst 229 # number of ReadReq
MSHR misses
system.cpu.l2cache.ReadReq_mshr_misses::cpu.data 71 # number of ReadReq
MSHR misses
system.cpu.l2cache.ReadReq_mshr_misses::total 300 # number of ReadReq
MSHR misses
system.cpu.l2cache.ReadExReq_mshr_misses::cpu.data 75 # number of
ReadExReq MSHR misses
system.cpu.l2cache.ReadExReq_mshr_misses::total 75 # number of ReadExReq
MSHR misses
system.cpu.l2cache.demand_mshr_misses::cpu.inst 229 # number of demand
(read+write) MSHR misses
system.cpu.l2cache.demand_mshr_misses::cpu.data 146 # number of demand
(read+write) MSHR misses
system.cpu.l2cache.demand_mshr_misses::total 375 # number of demand
(read+write) MSHR misses
system.cpu.l2cache.overall_mshr_misses::cpu.inst 229 # number of overall
MSHR misses
system.cpu.l2cache.overall_mshr_misses::cpu.data 146 # number of overall
MSHR misses
system.cpu.l2cache.overall_mshr_misses::total 375 # number of overall
MSHR misses
system.cpu.l2cache.ReadReq_mshr_miss_latency::cpu.inst 14085000 # number
of ReadReq MSHR miss cycles
system.cpu.l2cache.ReadReq_mshr_miss_latency::cpu.data 4569250 # number
of ReadReq MSHR miss cycles
system.cpu.l2cache.ReadReq_mshr_miss_latency::total 18654250 # number of
ReadReq MSHR miss cycles
system.cpu.l2cache.ReadExReq_mshr_miss_latency::cpu.data 4180250 #
number of ReadExReq MSHR miss cycles
system.cpu.l2cache.ReadExReq_mshr_miss_latency::total 4180250 # number
of ReadExReq MSHR miss cycles
system.cpu.l2cache.demand_mshr_miss_latency::cpu.inst 14085000 # number
of demand (read+write) MSHR miss cycles
system.cpu.l2cache.demand_mshr_miss_latency::cpu.data 8749500 # number
of demand (read+write) MSHR miss cycles
system.cpu.l2cache.demand_mshr_miss_latency::total 22834500 # number of
demand (read+write) MSHR miss cycles
system.cpu.l2cache.overall_mshr_miss_latency::cpu.inst 14085000 # number
of overall MSHR miss cycles
system.cpu.l2cache.overall_mshr_miss_latency::cpu.data 8749500 # number
of overall MSHR miss cycles
system.cpu.l2cache.overall_mshr_miss_latency::total 22834500 # number of
overall MSHR miss cycles
system.cpu.l2cache.ReadReq_mshr_miss_rate::cpu.inst 0.995652 # mshr miss
rate for ReadReq accesses
system.cpu.l2cache.ReadReq_mshr_miss_rate::cpu.data 1 # mshr miss rate
for ReadReq accesses
system.cpu.l2cache.ReadReq_mshr_miss_rate::total 0.996678 # mshr miss
rate for ReadReq accesses
system.cpu.l2cache.ReadExReq_mshr_miss_rate::cpu.data 1 # mshr miss rate
for ReadExReq accesses
system.cpu.l2cache.ReadExReq_mshr_miss_rate::total 1 # mshr miss rate
for ReadExReq accesses
system.cpu.l2cache.demand_mshr_miss_rate::cpu.inst 0.995652 # mshr miss
rate for demand accesses
system.cpu.l2cache.demand_mshr_miss_rate::cpu.data 1 # mshr miss rate
for demand accesses
system.cpu.l2cache.demand_mshr_miss_rate::total 0.997340 # mshr miss
rate for demand accesses
system.cpu.l2cache.overall_mshr_miss_rate::cpu.inst 0.995652 # mshr miss
rate for overall accesses
system.cpu.l2cache.overall_mshr_miss_rate::cpu.data 1 # mshr miss rate
for overall accesses
system.cpu.l2cache.overall_mshr_miss_rate::total 0.997340 # mshr miss
rate for overall accesses
system.cpu.l2cache.ReadReq_avg_mshr_miss_latency::cpu.inst 61506.550218
# average ReadReq mshr miss latency
system.cpu.l2cache.ReadReq_avg_mshr_miss_latency::cpu.data 64355.633803
# average ReadReq mshr miss latency
system.cpu.l2cache.ReadReq_avg_mshr_miss_latency::total 62180.833333 #
average ReadReq mshr miss latency
system.cpu.l2cache.ReadExReq_avg_mshr_miss_latency::cpu.data
55736.666667 # average ReadExReq mshr miss latency
system.cpu.l2cache.ReadExReq_avg_mshr_miss_latency::total 55736.666667 #
average ReadExReq mshr miss latency
system.cpu.l2cache.demand_avg_mshr_miss_latency::cpu.inst 61506.550218 #
average overall mshr miss latency
system.cpu.l2cache.demand_avg_mshr_miss_latency::cpu.data 59928.082192 #
average overall mshr miss latency
system.cpu.l2cache.demand_avg_mshr_miss_latency::total 60892 # average
overall mshr miss latency
system.cpu.l2cache.overall_avg_mshr_miss_latency::cpu.inst 61506.550218
# average overall mshr miss latency
system.cpu.l2cache.overall_avg_mshr_miss_latency::cpu.data 59928.082192
# average overall mshr miss latency
system.cpu.l2cache.overall_avg_mshr_miss_latency::total 60892 # average
overall mshr miss latency
system.cpu.l2cache.no_allocate_misses 0 # Number of misses that were
no-allocate
system.l2bus.trans_dist::ReadReq 301 # Transaction distribution
system.l2bus.trans_dist::ReadResp 301 # Transaction distribution
system.l2bus.trans_dist::Writeback 1 # Transaction distribution
system.l2bus.trans_dist::ReadExReq 75 # Transaction distribution
system.l2bus.trans_dist::ReadExResp 75 # Transaction distribution
system.l2bus.pkt_count_system.cpu.icache.mem_side::system.cpu.l2cache.cpu_side
460 # Packet count per connected master and slave (bytes)
system.l2bus.pkt_count_system.cpu.dcache.mem_side::system.cpu.l2cache.cpu_side
293 # Packet count per connected master and slave (bytes)
system.l2bus.pkt_count::total 753 # Packet count per connected master
and slave (bytes)
system.l2bus.pkt_size_system.cpu.icache.mem_side::system.cpu.l2cache.cpu_side
14720 # Cumulative packet size per connected master and slave (bytes)
system.l2bus.pkt_size_system.cpu.dcache.mem_side::system.cpu.l2cache.cpu_side
9408 # Cumulative packet size per connected master and slave (bytes)
system.l2bus.pkt_size::total 24128 # Cumulative packet size per
connected master and slave (bytes)
system.l2bus.snoops 0 # Total snoops (count)
system.l2bus.snoop_fanout::samples 377 # Request fanout histogram
system.l2bus.snoop_fanout::mean 1 # Request fanout histogram
system.l2bus.snoop_fanout::stdev 0 # Request fanout histogram
system.l2bus.snoop_fanout::underflows 0 0.00% 0.00% # Request fanout
histogram
system.l2bus.snoop_fanout::0 0 0.00% 0.00% # Request fanout histogram
system.l2bus.snoop_fanout::1 377 100.00% 100.00% # Request fanout histogram
system.l2bus.snoop_fanout::2 0 0.00% 100.00% # Request fanout histogram
system.l2bus.snoop_fanout::overflows 0 0.00% 100.00% # Request fanout
histogram
system.l2bus.snoop_fanout::min_value 1 # Request fanout histogram
system.l2bus.snoop_fanout::max_value 1 # Request fanout histogram
system.l2bus.snoop_fanout::total 377 # Request fanout histogram
system.l2bus.reqLayer0.occupancy 190500 # Layer occupancy (ticks)
system.l2bus.reqLayer0.utilization 0.0 # Layer utilization (%)
system.l2bus.respLayer0.occupancy 625000 # Layer occupancy (ticks)
system.l2bus.respLayer0.utilization 0.0 # Layer utilization (%)
system.l2bus.respLayer1.occupancy 395500 # Layer occupancy (ticks)
system.l2bus.respLayer1.utilization 0.0 # Layer utilization (%)
system.membus.trans_dist::ReadReq 300 # Transaction distribution
system.membus.trans_dist::ReadResp 300 # Transaction distribution
system.membus.trans_dist::ReadExReq 75 # Transaction distribution
system.membus.trans_dist::ReadExResp 75 # Transaction distribution
system.membus.pkt_count_system.cpu.l2cache.mem_side::system.mem_ctrl.port 750
# Packet count per connected master and slave (bytes)
system.membus.pkt_count_system.cpu.l2cache.mem_side::total 750 # Packet
count per connected master and slave (bytes)
system.membus.pkt_count::total 750 # Packet count per connected master
and slave (bytes)
system.membus.pkt_size_system.cpu.l2cache.mem_side::system.mem_ctrl.port
24000 # Cumulative packet size per connected master and slave (bytes)
system.membus.pkt_size_system.cpu.l2cache.mem_side::total 24000 #
Cumulative packet size per connected master and slave (bytes)
system.membus.pkt_size::total 24000 # Cumulative packet size per
connected master and slave (bytes)
system.membus.snoops 0 # Total snoops (count)
system.membus.snoop_fanout::samples 375 # Request fanout histogram
system.membus.snoop_fanout::mean 0 # Request fanout histogram
system.membus.snoop_fanout::stdev 0 # Request fanout histogram
system.membus.snoop_fanout::underflows 0 0.00% 0.00% # Request fanout
histogram
system.membus.snoop_fanout::0 375 100.00% 100.00% # Request fanout
histogram
system.membus.snoop_fanout::1 0 0.00% 100.00% # Request fanout histogram
system.membus.snoop_fanout::overflows 0 0.00% 100.00% # Request fanout
histogram
system.membus.snoop_fanout::min_value 0 # Request fanout histogram
system.membus.snoop_fanout::max_value 0 # Request fanout histogram
system.membus.snoop_fanout::total 375 # Request fanout histogram
system.membus.reqLayer2.occupancy 187500 # Layer occupancy (ticks)
system.membus.reqLayer2.utilization 0.0 # Layer utilization (%)
system.membus.respLayer0.occupancy 1018000 # Layer occupancy (ticks)
system.membus.respLayer0.utilization 0.0 # Layer utilization (%)

