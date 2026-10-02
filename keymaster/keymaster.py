import re
import textwrap
from z3 import *
 
BODY = r""" uVar38 = (uint)local_148;
uVar8 = (uint)local_13d;
uVar26 = (uint)local_145;
uVar19 = (uint)local_138;
bVar59 = uVar38 * local_142 + uVar26 + uVar8 * local_147 != 0x4bb4;
uVar27 = (uint)local_131;
uVar11 = (uint)local_137;
uVar2 = (uint)bVar59;
uVar28 = (uint)local_133;
if (uVar11 * local_128 + uVar19 * uVar27 + uVar28 != 0x32e3) {
uVar2 = bVar59 + 1;
}
uVar12 = (uint)local_121;
uVar25 = (uint)local_13f;
uVar9 = (uint)local_126;
if (uVar38 * uVar25 + uVar12 * uVar9 + uVar8 * uVar27 + (uint)(local_134 ^ local_125) !=
0x43c1) {
uVar2 = uVar2 + 1;
}
uVar20 = (uint)local_123;
if ((uint)(local_12d ^ local_124) + (uint)(local_145 ^ local_12b) +
(uint)(local_12d ^ local_12f) + uVar38 * local_123 + uVar28 != 0x2e17) {
uVar2 = uVar2 + 1;
}
uVar39 = (uint)local_140;
local_1c4 = CONCAT13(local_130,CONCAT12(local_146,CONCAT11(local_124,local_134)));
uVar4 = (uint)local_130;
if (uVar28 * local_140 + (uint)(local_146 ^ local_140) + (uint)(local_13e ^ local_146) +
uVar19 * uVar4 + uVar8 + (uint)local_128 != 0x496a) {
uVar2 = uVar2 + 1;
}
uVar29 = (uint)local_136;
uVar35 = (uint)local_128;
if ((local_126 ^ local_144) + uVar4 + uVar29 * uVar35 != 0x23ae) {
uVar2 = uVar2 + 1;
}
uVar37 = (uint)local_146;
uVar21 = (uint)local_122;
uVar30 = (uint)local_12d;
if (uVar37 + uVar21 * uVar35 + uVar30 != 0x2bee) {
uVar2 = uVar2 + 1;
}
iVar22 = uVar28 * local_13c;
uVar31 = (uint)local_124;
uVar40 = (uint)local_129;
if (iVar22 + local_124 * uVar40 + (uint)(local_142 ^ local_135) + (uint)local_13c +
(uint)(local_13f ^ local_124) + uVar30 != 0x5fc5) {
uVar2 = uVar2 + 1;
}
uVar14 = (uint)local_134;
uVar45 = (uint)local_12a;
local_1e0 = CONCAT13(local_13a,CONCAT12(local_135,CONCAT11(local_13c,local_12d)));
uVar57 = (uint)local_13a;
if ((uint)(local_147 ^ local_133) +
uVar35 * uVar4 + uVar31 * uVar14 + (uint)(local_12a ^ local_13a) + local_13a * uVar35 +
(uint)local_12a * (uint)local_12f != 0xb7c9) {
uVar2 = uVar2 + 1;
}
iVar32 = uVar21 * local_147;
if ((local_146 ^ local_12e) + uVar31 + uVar38 + uVar37 + iVar32 != 0x343d) {
uVar2 = uVar2 + 1;
}
uVar23 = CONCAT11(local_128,local_12b) & 0xff;
uVar33 = (uint)local_135;
uVar6 = (uint)local_147;
uVar15 = (uint)local_139;
if (uVar23 * uVar4 + (uint)(local_145 ^ local_140) + uVar57 * uVar6 + uVar9 * uVar15 +
uVar12 * uVar33 != 0x8700) {
uVar2 = uVar2 + 1;
}
local_1d4._0_2_ = CONCAT11(local_143,local_12e);
uVar1 = (ushort)local_1d4;
local_1d4 = (uint)(ushort)local_1d4;
uVar24 = (uint)local_143;
uVar4 = (uint)local_13c;
if (uVar24 * uVar4 + uVar31 != 0x15ef) {
uVar2 = uVar2 + 1;
}
iVar16 = uVar40 * uVar45;
uVar42 = (uint)local_127;
local_200 = CONCAT13(local_127,CONCAT12(local_140,CONCAT11(local_13e,local_13d)));
iVar46 = uVar33 * local_13b;
local_1c0 = CONCAT22(CONCAT11(local_128,local_12b),CONCAT11(local_13b,local_129));
uVar44 = (local_148 ^ local_1c0) & 0xff;
if (uVar15 * uVar42 + uVar20 * uVar29 + uVar24 + iVar46 + uVar44 + iVar16 != 0x7ea8) {
uVar2 = uVar2 + 1;
}
if (local_142 + uVar21 + uVar19 + ((local_142 ^ local_1c0) & 0xff) +
(uint)(local_133 ^ local_12c) != 0x14a) {
uVar2 = uVar2 + 1;
}
uVar43 = (uint)local_144;
if (uVar28 * uVar43 + uVar35 + uVar40 * uVar6 != 0x41af) {
uVar2 = uVar2 + 1;
}
uVar47 = (uint)local_132;
uVar17 = (uint)local_12c;
if (uVar9 * uVar17 + (uint)(local_13b ^ local_12c) + uVar12 + uVar47 + uVar21 * local_142 +
uVar27 * uVar6 != 0x43c2) {
uVar2 = uVar2 + 1;
}
uVar13 = (uint)local_130;
if ((uint)(local_146 ^ local_122) + uVar27 * uVar20 + uVar19 + uVar17 + uVar30 * uVar13 !=
0x49f6) {
uVar2 = uVar2 + 1;
}
if (uVar13 * uVar4 + (uint)(local_145 ^ local_132) + uVar21 + (uint)(local_129 ^ local_127) !=
0x2fa0) {
uVar2 = uVar2 + 1;
}
uVar48 = (uint)local_13e;
if (uVar48 * uVar4 + (uint)(local_148 ^ local_142) + uVar45 * uVar13 + (uint)local_12f !=
0x5d34) {
uVar2 = uVar2 + 1;
}
uVar41 = (uint)local_12f;
iVar49 = uVar41 * local_13b;
if ((local_142 ^ local_136) + uVar8 + iVar49 != 0x1672) {
uVar2 = uVar2 + 1;
}
uVar50 = (uint)local_12e;
iVar51 = uVar14 * (uVar1 & 0xff);
if (uVar8 * uVar43 + iVar51 + (uint)(local_126 ^ local_122) != 0x43db) {
uVar2 = uVar2 + 1;
}
if (uVar29 + uVar40 + uVar13 + (uint)(local_146 ^ local_12c) + (uint)(local_13d ^ local_121)
!= 0x134) {
uVar2 = uVar2 + 1;
}
if (uVar9 * uVar29 + uVar27 * uVar14 + (uint)(local_127 ^ local_12c) + uVar38 * uVar15 !=
0x3e83) {
uVar2 = uVar2 + 1;
}
uVar18 = (uint)local_141;
if (uVar8 + uVar18 + uVar33 * uVar47 != 0x3510) {
uVar2 = uVar2 + 1;
}
uVar34 = (uint)local_142;
if (uVar9 * uVar34 + uVar17 + uVar11 * uVar50 != 0x329d) {
uVar2 = uVar2 + 1;
}
if (uVar50 * uVar35 + uVar15 * uVar41 + (uint)(local_148 ^ local_140) != 0x395f) {
uVar2 = uVar2 + 1;
}
if (uVar25 + uVar39 + uVar40 * uVar43 + uVar13 != 0x13cd) {
uVar2 = uVar2 + 1;
}
uVar52 = (local_13d ^ local_1d4) & 0xff;
if (((local_13f ^ local_1c4) & 0xff) + (uint)(local_148 ^ local_141) + uVar52 != 0x7f) {
uVar2 = uVar2 + 1;
}
iVar53 = uVar8 * uVar37;
if ((uint)(local_145 ^ local_127) +
(uint)(local_147 ^ local_13c) + uVar31 * uVar6 + uVar44 + iVar53 + uVar31 * uVar47 !=
0x9880) {
uVar2 = uVar2 + 1;
}
iVar54 = uVar12 * uVar50;
uVar44 = (uint)local_13b;
if (uVar57 * uVar4 + iVar54 + uVar50 * uVar44 + (uint)(local_13e ^ local_141) != 0x6f20) {
uVar2 = uVar2 + 1;
}
uVar55 = (uint)local_125;
if (uVar28 * uVar6 + uVar39 * uVar18 + uVar12 * uVar33 + uVar20 + uVar55 * uVar35 != 0xc3f5) {
uVar2 = uVar2 + 1;
}
iVar56 = uVar21 * uVar42;
if (uVar21 * uVar47 + ((local_148 ^ local_200) & 0xff) + uVar43 * uVar47 + iVar56 + uVar44 +
uVar14 * uVar14 != 0xb853) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_142 ^ local_139) + uVar20 * uVar15 + uVar30 + uVar27 * uVar55 != 0x284a) {
uVar2 = uVar2 + 1;
}
if (((local_145 ^ local_1c0) & 0xff) + uVar17 + iVar56 + uVar42 * uVar44 != 0x4b0f) {
uVar2 = uVar2 + 1;
}
if (uVar19 * uVar39 + uVar15 + (uint)(local_122 ^ local_13a) + uVar37 +
(uint)(local_125 ^ local_139) + (uint)(local_126 ^ local_124) != 0x1824) {
uVar2 = uVar2 + 1;
}
if (uVar13 * uVar42 + uVar57 + uVar19 * uVar57 + uVar23 + (uint)(local_145 ^ local_126) +
uVar38 != 0x4895) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_12d ^ local_139) + uVar23 * uVar6 + uVar19 + uVar31 + uVar45 * uVar17 !=
0x438b) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_142 ^ local_141) + uVar40 * uVar17 + uVar37 * uVar42 != 0x58e5) {
uVar2 = uVar2 + 1;
}
if (uVar9 * uVar55 + uVar11 * uVar21 + (uint)(local_12e ^ local_141) != 0x42e4) {
uVar2 = uVar2 + 1;
}
if (local_124 * uVar40 + uVar55 + uVar42 + (uint)(local_142 ^ local_123) + uVar18 != 0x2e95) {
uVar2 = uVar2 + 1;
}
if ((uVar17 + uVar20) * uVar4 + uVar6 * uVar13 != 0x8ba4) {
uVar2 = uVar2 + 1;
}
if (uVar9 * uVar20 + uVar38 + uVar12 != 0x1558) {
uVar2 = uVar2 + 1;
}
if (uVar15 * uVar43 + uVar21 * uVar45 + uVar37 * uVar41 + uVar57 * uVar24 +
(uint)(local_147 ^ local_136) != 0x7ec4) {
uVar2 = uVar2 + 1;
}
if (uVar37 * uVar37 + uVar13 + (uint)(local_128 ^ local_124) != 0x2baa) {
uVar2 = uVar2 + 1;
}
uVar13 = (uint)local_128;
if ((local_134 ^ local_13e) + uVar57 + iVar22 + uVar35 * uVar13 +
(uint)(local_142 ^ local_133) + uVar55 != 0x55d1) {
uVar2 = uVar2 + 1;
}
if (uVar9 * uVar23 + uVar30 * uVar23 + (uint)(local_13e ^ local_139) + uVar6 * uVar13 +
(uint)(local_145 ^ local_128) + uVar18 != 0x4c80) {
uVar2 = uVar2 + 1;
}
if (uVar28 * uVar14 + (uint)(local_145 ^ local_132) + uVar37 * uVar41 + uVar9 * uVar33 !=
0x7b5c) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_134 ^ local_12a) + uVar13 * uVar41 + iVar53 != 0x5c63) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_13c ^ local_12b) + uVar23 + uVar42 + uVar12 * uVar20 +
(uint)(local_147 ^ local_12b) != 0x3680) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_139 ^ local_143) + (uint)local_142 + (uint)local_12f + uVar26 * uVar18 +
uVar23 + uVar57 != 0x1952) {
uVar2 = uVar2 + 1;
}
if (uVar28 * uVar40 + (uint)(local_13f ^ local_125) + uVar38 * uVar4 != 0x5b55) {
uVar2 = uVar2 + 1;
}
if (uVar23 * uVar4 +
uVar9 * uVar39 + (uint)(local_142 ^ local_13e) + (uint)(local_143 ^ local_127) + uVar52 +
uVar38 * uVar44 != 0x3fc0) {
uVar2 = uVar2 + 1;
}
uVar52 = (uint)local_12f;
if (uVar30 * uVar37 + uVar38 * uVar29 + (uint)(local_13d ^ local_12c) + uVar52 +
uVar20 * uVar37 + uVar25 != 0x86be) {
uVar2 = uVar2 + 1;
}
if (uVar30 * uVar45 + uVar52 * uVar18 + uVar33 + uVar25 * uVar18 +
(uint)(local_13d ^ local_124) != 0x81da) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_124 ^ local_12a) + uVar34 * uVar18 + (uint)(local_126 ^ local_12c) != 0x1a6a)
{
uVar2 = uVar2 + 1;
}
if (uVar24 * uVar17 + uVar15 + uVar25 * uVar42 != 0x2a73) {
uVar2 = uVar2 + 1;
}
uVar7 = (uint)local_147;
iVar58 = uVar43 * uVar55;
if (uVar39 + iVar58 + uVar7 * uVar4 != 0x4260) {
uVar2 = uVar2 + 1;
}
if (uVar30 * uVar23 + uVar47 + (local_136 ^ local_13a) + uVar38 * uVar57 +
(uint)(local_147 ^ local_139) != 0x4691) {
uVar2 = uVar2 + 1;
}
uVar4 = (uint)local_130;
if (uVar29 * uVar4 + uVar40 * uVar57 + uVar8 * uVar11 + (uint)(local_137 ^ local_130) + iVar58
+ (uint)(local_140 ^ local_13b) != 0x9824) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_13d ^ local_141) + uVar15 * uVar4 + uVar34 * uVar42 + uVar45 * uVar42 !=
0x5e47) {
uVar2 = uVar2 + 1;
}
if (uVar19 * uVar47 + uVar4 + uVar21 != 0x1871) {
uVar2 = uVar2 + 1;
}
if ((local_121 ^ local_13e) + uVar34 + (uint)(local_125 ^ local_140) +
(uint)(local_123 ^ local_135) != 0x94) {
uVar2 = uVar2 + 1;
}
if (((local_121 ^ local_1d4) & 0xff) + ((local_133 ^ local_1c4) & 0xff) + uVar27 +
uVar23 * uVar13 + (uint)(local_148 ^ local_143) != 0x13a5) {
uVar2 = uVar2 + 1;
}
if (uVar33 + iVar51 + uVar42 + uVar57 + uVar19 * uVar37 != 0x438f) {
uVar2 = uVar2 + 1;
}
uVar5 = (uint)local_13c;
if ((local_136 ^ local_13a) + uVar28 + uVar31 * uVar5 + uVar38 * uVar52 +
(uint)(local_147 ^ local_131) != 0x6263) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_122 ^ local_12c) + (uint)(local_128 ^ local_135) + uVar40 * 2 != 0x111) {
uVar2 = uVar2 + 1;
}
if (uVar33 * uVar50 + (local_133 ^ local_13e) + uVar50 + uVar24 * uVar7 != 0x410b) {
uVar2 = uVar2 + 1;
}
if (uVar20 * uVar55 + uVar11 * uVar7 + (uint)(local_130 ^ local_143) +
(uint)(local_121 ^ local_12b) + uVar52 != 0x58d3) {
uVar2 = uVar2 + 1;
}
if (uVar9 * uVar42 + uVar26 * uVar55 + uVar27 * uVar29 != 0x3b3b) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_126 ^ local_137) + uVar17 * uVar18 + (uint)(local_138 ^ local_141) +
(uint)(local_13a ^ local_127) + uVar43 + uVar25 != 0x3397) {
uVar2 = uVar2 + 1;
}
if (uVar14 * uVar5 + (uint)(local_13e ^ local_139) + uVar21 + uVar8 + uVar34 * uVar4 + uVar57
!= 0x4cb3) {
uVar2 = uVar2 + 1;
}
if (uVar5 * uVar44 + uVar43 * uVar4 + uVar26 != 0x2942) {
uVar2 = uVar2 + 1;
}
if (uVar27 * uVar48 + uVar31 * uVar50 + (uint)(local_142 ^ local_13b) + uVar17 * uVar55 +
uVar55 + (uint)(local_137 ^ local_12c) != 0x6792) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_13f ^ local_140) + iVar56 + iVar22 + (uint)(local_138 ^ local_143) +
(uint)(local_13c ^ local_13b) + (uint)(local_13e ^ local_135) != 0x66bd) {
uVar2 = uVar2 + 1;
}
if (uVar23 * uVar47 + uVar50 + uVar15 * uVar50 != 0x29aa) {
uVar2 = uVar2 + 1;
}
if (uVar37 + uVar30 * uVar50 + (uint)(local_13d ^ local_140) + uVar33 + uVar17 != 0x2e35) {
uVar2 = uVar2 + 1;
}
if (uVar38 * uVar23 + iVar16 + (uint)(local_12d ^ local_13a) + uVar33 != 0x4008) {
uVar2 = uVar2 + 1;
}
if (iVar32 + uVar11 * uVar21 + uVar25 * uVar21 != 0x7970) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_122 ^ local_13c) + iVar16 + uVar26 * uVar5 != 0x3fc6) {
uVar2 = uVar2 + 1;
}
if (uVar26 * uVar37 + uVar19 * uVar23 + (uint)(local_142 ^ local_13a) + uVar15 + uVar7 +
uVar19 * uVar27 != 0x2a36) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_134 ^ local_135) + (uint)(local_143 ^ local_141) + uVar47 * uVar37 +
(uint)(local_125 ^ local_146) != 0x301d) {
uVar2 = uVar2 + 1;
}
if (uVar34 * uVar34 + uVar8 * uVar30 + uVar40 * uVar44 + ((local_12f ^ local_1d4) & 0xff) !=
0x5781) {
uVar2 = uVar2 + 1;
}
if (uVar15 * uVar18 +
(uint)local_147 + (uint)(local_137 ^ local_13e) + (uint)(local_12f ^ local_139) +
uVar21 * uVar35 + uVar11 * uVar20 != 0x7145) {
uVar2 = uVar2 + 1;
}
if (uVar38 * uVar40 + uVar52 + uVar44 + (uint)(local_137 ^ local_127) + uVar40 * uVar6 +
(uint)(local_147 ^ local_135) != 0x564a) {
uVar2 = uVar2 + 1;
}
if (uVar11 * uVar37 + uVar24 * uVar47 + uVar43 * uVar50 + uVar29 + uVar48 * uVar47 != 0x8613)
{
uVar2 = uVar2 + 1;
}
uVar35 = (uint)local_142;
if ((local_140 ^ local_12c) + uVar34 + iVar51 + uVar45 + uVar48 * uVar35 != 0x446a) {
uVar2 = uVar2 + 1;
}
if (uVar38 * uVar30 + uVar13 + (uint)(local_13d ^ local_137) + iVar46 + uVar47 * uVar52 !=
0x7cb3) {
uVar2 = uVar2 + 1;
}
if (uVar12 * uVar7 + uVar33 + uVar8 * uVar5 + (uint)(local_12d ^ local_127) +
(uint)(local_124 ^ local_125) != 0x6b5a) {
uVar2 = uVar2 + 1;
}
if (uVar43 * uVar44 +
(uint)(local_138 ^ local_139) + uVar31 * uVar48 + (uint)(local_128 ^ local_130) +
uVar25 * uVar27 != 0x434b) {
uVar2 = uVar2 + 1;
}
if (uVar30 + uVar48 + ((local_135 ^ local_1d4) & 0xff) + (uint)(local_13d ^ local_13b) !=
0x15a) {
uVar2 = uVar2 + 1;
}
uVar25 = (uint)local_13b;
if (uVar12 * uVar15 + uVar50 * uVar52 + uVar25 != 0x42ca) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_133 ^ local_12b) + (uint)(local_148 ^ local_143) + uVar30 * uVar50 +
uVar13 * uVar41 + uVar17 * uVar25 != 0x6bdd) {
uVar2 = uVar2 + 1;
}
if (uVar43 * uVar17 + uVar19 * uVar42 + uVar29 * uVar57 + uVar29 * uVar15 + uVar38 * local_123
+ ((local_121 ^ local_1c0) & 0xff) != 0x938a) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_12d ^ local_141) + uVar42 * uVar29 + uVar5 != 0x2b7c) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_148 ^ local_132) + (uint)(local_137 ^ local_13e) + uVar28 != 0x92) {
uVar2 = uVar2 + 1;
}
if (uVar4 + (local_147 ^ local_127) + (uint)(local_133 ^ local_122) != 0x78) {
uVar2 = uVar2 + 1;
}
if (uVar24 * uVar35 + (uint)(local_135 ^ local_122) + iVar54 + (uint)(local_148 ^ local_13c) +
(uint)(local_129 ^ local_12a) + (uint)(local_146 ^ local_130) != 0x3907) {
uVar2 = uVar2 + 1;
}
if (uVar14 * uVar23 + uVar38 * uVar27 + iVar54 + uVar39 + uVar48 * uVar52 != 0x8cc3) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_12d ^ local_140) + (uint)(local_13b ^ local_122) +
(uint)(local_136 ^ local_127) + uVar13 * uVar17 != 0x276f) {
uVar2 = uVar2 + 1;
}
if (local_12f * uVar40 + (uint)(local_145 ^ local_13c) + (uint)(local_13a ^ local_132) +
uVar43 * uVar24 != 0x36c1) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_13d ^ local_122) + (uint)(local_142 ^ local_13b) + uVar31 * uVar5 != 0x317d)
{
uVar2 = uVar2 + 1;
}
if ((uint)(local_142 ^ local_12c) + uVar26 * uVar30 + uVar5 * uVar35 + uVar28 + uVar35 !=
0x2fde) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_127 ^ local_132) +
((local_128 ^ local_1e0) & 0xff) + (uint)(local_12c ^ local_136) + uVar19 * uVar40 +
(uint)(local_136 ^ local_143) != 0x1519) {
uVar2 = uVar2 + 1;
}
if (uVar33 * uVar35 + uVar29 * uVar15 + ((local_13a ^ local_1d4) & 0xff) + uVar47 * uVar37 +
uVar12 * uVar31 + iVar49 != 0xa7ee) {
uVar2 = uVar2 + 1;
}
if (uVar11 * uVar57 + uVar20 * uVar37 + (uint)(local_136 ^ local_127) + uVar19 * uVar15 !=
0x64d0) {
uVar2 = uVar2 + 1;
}
if (uVar29 * uVar33 + (uint)(local_13c ^ local_13f) + (uint)(local_142 ^ local_136) +
uVar25 * uVar18 + (uint)(local_13f ^ local_13e) != 0x42e0) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_13c ^ local_144) + uVar40 * uVar24 + (uint)(local_12a ^ local_125) != 0x1419)
{
uVar2 = uVar2 + 1;
}
if ((local_133 ^ local_140) + uVar28 + uVar23 * uVar48 != 0x15fa) {
uVar2 = uVar2 + 1;
}
if (uVar7 * uVar14 + (uint)(local_139 ^ local_141) + uVar18 + uVar57 * uVar6 +
(uint)(local_12a ^ local_13a) != 0x6566) {
uVar2 = uVar2 + 1;
}
if ((uint)(local_127 ^ local_12c) + uVar20 * uVar24 * 2 != 0x2ab1) {
uVar2 = uVar2 + 1;
}
uVar38 = uVar38 * uVar37 + (uint)(local_144 ^ local_130);
if ((uint)local_13b + uVar48 * 2 + uVar38 != 0x2d48) {
uVar2 = uVar2 + 1;
}
if ((local_130 ^ local_132) + uVar57 + iVar53 + uVar11 + uVar19 * uVar30 != 0x4b27) {
uVar2 = uVar2 + 1;
}
if (uVar8 * uVar18 + uVar47 * uVar52 + uVar17 + uVar18 + (uint)(local_121 ^ local_125) !=
0x6f45) {
uVar2 = uVar2 + 1;
}
if (uVar48 * uVar20 + uVar50 * uVar55 + uVar11 * uVar50 + uVar21 * uVar23 +
(uint)(local_147 ^ local_136) != 0x909c) {
uVar2 = uVar2 + 1;
}
if (uVar12 * uVar47 + uVar8 + (uint)(local_121 ^ local_13a) + ((local_125 ^ local_1e0) & 0xff)
!= 0x3953) {
uVar2 = uVar2 + 1;
}
if (uVar26 * uVar39 + uVar43 * uVar24 + uVar12 + uVar47 * uVar35 +
(uint)(local_126 ^ local_124) != 0x3878) {
uVar2 = uVar2 + 1;
}
if (uVar12 * uVar25 + iVar58 + uVar31 + uVar14 * uVar25 != 0x4063) {
uVar2 = uVar2 + 1;
}
"""
 
def CONCAT11(a, b): return (a * 256) + (b & 0xff)
def CONCAT12(a, b): return (a * 65536) + (b & 0xffff)
def CONCAT13(a, b): return (a * 16777216) + (b & 0xffffff)
def CONCAT22(a, b): return (a * 65536) + (b & 0xffff)
 
 
def loc(h, b):
return b[0x148 - int(h, 16)]
 
 
def build_and_solve():
text = BODY
 
text = re.sub(r'\((?:uint|int|ulonglong|ushort|undefined4|undefined2|undefined1|byte)\)', '', text)
text = text.replace('._0_2_', '')
 
# local_148..local_121 (40 байт входа) -> b[0]..b[39]
mapping = {f'local_{0x148 - i:x}': f'b[{i}]' for i in range(40)}
text = re.sub(r'local_[0-9a-f]{3}\b', lambda m: mapping.get(m.group(0), m.group(0)), text)
 
text = re.sub(r'\)\s*\n\s*\{', ') {', text)
 
def bvar_repl(m):
expr, const = m.group(1).strip(), m.group(2)
return f's.add(({expr}) == {const})\nbVar59 = False\n'
text = re.sub(r'bVar59\s*=\s*(.*?)!=\s*(0x[0-9a-fA-F]+);',
bvar_repl, text, count=1, flags=re.DOTALL)
 
pattern = re.compile(r'if\s*\((.*?)!=\s*(0x[0-9a-fA-F]+)\)\s*\{(.*?)\}', re.DOTALL)
text = pattern.sub(lambda m: f's.add(({m.group(1).strip()}) == {m.group(2)})\n', text)
 
text = '\n'.join(line.lstrip() for line in text.splitlines())
 
b = [BitVec(f'b{i}', 32) for i in range(40)]
s = Solver()
for x in b:
s.add(x >= 0x20, x <= 0x7e) 
 
env = {'b': b, 's': s,
'CONCAT11': CONCAT11, 'CONCAT12': CONCAT12,
'CONCAT13': CONCAT13, 'CONCAT22': CONCAT22}
 
exec(compile(text, '<check>', 'exec'), env)
 
s.add((loc('12e', b) ^ loc('143', b)) + env['uVar27'] * env['uVar15'] +
(loc('137', b) ^ loc('12b', b)) + (loc('12f', b) ^ loc('140', b)) +
(loc('148', b) ^ loc('131', b)) + env['uVar24'] == 0xb1c)
s.add((loc('12b', b) ^ loc('141', b)) + env['uVar35'] +
env['uVar11'] * env['uVar45'] == 0x2e0e)
s.add(env['uVar20'] * env['uVar33'] + env['uVar9'] == 0x3127)
 
if s.check() != sat:
raise SystemExit("unsat ")
 
m = s.model()
return ''.join(chr(m[x].as_long()) for x in b)
 
 
if __name__ == "__main__":
print("FLAG:", build_and_solve())
