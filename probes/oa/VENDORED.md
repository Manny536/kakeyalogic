# VENDORED: OA probe (PROPOSED / ONGOING)

Source: cwi-main commit `97064b1` (branch `feat/oa-probe`, local; origin agreeya-org1-scout/CoWork-Inference).

## Upstream sha256 at that commit

- `kakeya_checks/causal.py` `56557f32deaab97a3674148d7c7cf1890ec0221b5babd7c82ac930b524ab207f`
- `kakeya_checks/oa_probe.py` `ac1caec7bc27d192e9897029eb22556668f70c4f85d5fe6b64a90a22a7501cbc`
- `docs/OA_PROBE_PREREG.json` `0bbecb50e7ff3dc27ee1d0b7fb5869ae7ee76043829ed43f746b5dd4ac7a8138`
- `docs/OA_PROBE_RESULTS_v2.json` `8c7e1db61c65bf17b39252725224e3227d9788ca04db7b5b0ae133797c382ace`

## sha256 of the files as vendored here

- `docs/OA_PROBE.md` `5f8ff51837668795e333f3342cabcaf5b0c65fd8f41f9d8bd50a3fe7d395c4bd`
- `docs/OA_PROBE_EXPLORATORY_C.json` `e4a3396c80fbfa69ebedaedb42fdedb49955399488befa7d4f3f030ce7b99978`
- `docs/OA_PROBE_PREREG.json` `0bbecb50e7ff3dc27ee1d0b7fb5869ae7ee76043829ed43f746b5dd4ac7a8138`
- `docs/OA_PROBE_RESULTS.json` `7ddef9db43bc8f67023d9e247a3476ed567b4802b4fa2fcf8097f62f13360563`
- `docs/OA_PROBE_RESULTS_v2.json` `8c7e1db61c65bf17b39252725224e3227d9788ca04db7b5b0ae133797c382ace`
- `probe_tests/oa/oa_mutants.py` `33f2bdeb7c627993dbc2fd015581c66828c250448c487cc5cfc632ce9f23b363`
- `probe_tests/oa/test_oa_probe.py` `4edad8154ec57a262e13c2f4be8118cb5198bc0a48b80a25721c2df4fb30d54b`
- `probes/oa/__init__.py` `12590f3fe1cc30f2b5837bda8ef980097587e7d58e293fab3eacd096c6ea0a93`
- `probes/oa/causal.py` `56557f32deaab97a3674148d7c7cf1890ec0221b5babd7c82ac930b524ab207f`
- `probes/oa/oa_probe.py` `ac1caec7bc27d192e9897029eb22556668f70c4f85d5fe6b64a90a22a7501cbc`
- `scripts/oa_experiment.py` `678a0e621b0749243f8f39403f8249ac5704b9b56a2fb80d7b4f27dc8da9672a`
- `scripts/oa_mutation_smoke.py` `f616e00dde9559d89b32f3955740202539b0186e33079de8ba40eee0817e8212`

Byte-identical to upstream: docs/OA_PROBE_PREREG.json, docs/OA_PROBE_RESULTS_v2.json (tests pin the prereg hash and compare outcomes to the committed results).
Changed on vendoring: import paths, test-dir paths; causal.py and oa_probe.py otherwise unmodified.

ANALOGY ONLY: the paper (arXiv:2501.02305) is about hash tables, not agents; nothing here certifies an agent or closes L²_C.
