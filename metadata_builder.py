import json

def build(jd):
    actual_data = f"""#pragma once

    #include "json.hpp"

// =====================================================================
//  Embedded INFRA map metadata (per-map maximum counter values).
//
//  These DEFAULT values already incorporate MrMagnetix's "INFRA Success
//  Counters FIX" (speedrun.com/infra/resources/mjtgi), which corrects
//  the wrong maximum photo/corruption counts present in the original
//  Success Counters mod. Corrected entries vs. the old data:
//      c3_m2_tunnel2  cameras   11 -> 9
//      c5_m1_watertr. cameras   16 -> 17
//      c5_m2b_sewer2  cameras   10 -> 11
//      c6_m6_central  cameras    3 -> 4   (defect/corruption were swapped)
//      c6_m6_central  corruption 4 -> 3
//      c7_m2_bunker   cameras   17 -> 11
//      c7_m2_bunker   corruption 7 -> 13
//      c7_m3_stormd.  cameras   29 -> 32
//      c7_m4_cistern  cameras   19 -> 21
//      c8_m7_business2 cameras  10 -> 11
//      c10_m1_npp     cameras   12 -> 14
//
//  At runtime the mod will ALSO look for an external "mapdata.txt" next
//  to infra.exe and prefer it if present (see counters.cpp::LoadMapData).
//  That makes the speedrun FIX file a drop-in, and lets you tweak counts
//  without rebuilding. This embedded copy is the fallback.
// =====================================================================

auto g_mapdata = R"(
{json.dumps(jd, indent=4)}
)"_json;
    """
    return actual_data
