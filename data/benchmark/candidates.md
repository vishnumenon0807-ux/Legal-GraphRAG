# Annotation worklist

Top 120 of 228 cross-section reference edges, ranked by
how hard the target would be for a retriever that only sees the anchor.

For each one worth using, write a question whose natural answer needs BOTH
clauses, then add it to `questions.jsonl`. Skip freely: a forced question is
worse than a smaller dataset. Aim for roughly 200 kept.

---

## 1. s38(1) -> s447

score 0.8403 | dissimilarity 0.9588 | target in-degree 13 | trigger `under`

**Anchor s38(1)** (Punishment for personation for acquisition, etc., of securities.)

> Any person who— (a) makes or abets making of an application in a fictitious name to a company for acquiring, or subscribing for, its securities; or (b) makes or abets making of multiple applications to a company in different names or in different combinations of his name or surname for acquiring or 

**Target s447** (Punishment for fraud.)

> Without prejudice to any liability including repayment of any debt under this Act or any other law for the time being in force, any person who is found to be guilty of fraud, shall be punishable with imprisonment for a term which shall not be less than six months but which may extend to ten years an

```
question:
answer:
gold_clauses: ["s38(1)", "s447"]
anchor_clause: "s38(1)"
reference_path: [["s38(1)", "s447"]]
difficulty: one_hop
```

---

## 2. s137(3) -> s403

score 0.8173 | dissimilarity 0.883 | target in-degree 13 | trigger `specified in`

**Anchor s137(3)** (Copy of financial statement to be filed with Registrar.)

> If a company fails to file the copy of the financial statements under sub-section (1) or sub-section (2), as the case may be, before the expiry of the period specified in section 403, the company shall be punishable with fine of one thousand rupees for every day during which the failure continues bu

**Target s403** (Fee for filing, etc.)

> (1) Any document, required to be submitted, filed, registered or recorded, or any fact or information required or authorised to be registered under this Act, shall be submitted, filed, registered or recorded within the time specified in the relevant provision on payment of such fee as may be prescri

```
question:
answer:
gold_clauses: ["s137(3)", "s403"]
anchor_clause: "s137(3)"
reference_path: [["s137(3)", "s403"]]
difficulty: one_hop
```

---

## 3. s149(9) -> s198

score 0.7697 | dissimilarity 0.9545 | target in-degree 4 | trigger `subject to the provisions of`

**Anchor s149(9)** (Company to have Board of Directors.)

> Notwithstanding anything contained in any other provision of this Act, but subject to the provisions of sections 197 and 198, an independent director shall not be entitled to any stock option and may receive remuneration by way of fee provided under sub-section (5) of section 197, reimbursement of e

**Target s198** (Calculation of profits.)

> (1) In computing the net profits of a company in any financial year for the purpose of section 197,— (a) credit shall be given for the sums specified in sub-section (2), and credit shall not be given for those specified in sub-section (3); and (b) the sums specified in sub-section (4) shall be deduc

```
question:
answer:
gold_clauses: ["s149(9)", "s198"]
anchor_clause: "s149(9)"
reference_path: [["s149(9)", "s198"]]
difficulty: one_hop
```

---

## 4. s233(12) -> s230

score 0.736 | dissimilarity 0.9593 | target in-degree 6 | trigger `referred to in`

**Anchor s233(12)** (Merger or amalgamation of certain companies.)

> The provisions of this section shall mutatis mutandis apply to a company or companies specified in sub-section (1) in respect of a scheme of compromise or arrangement referred to in section 230 or division or transfer of a company referred to clause (b) of subsection (1) of section 232.

**Target s230** (Power to compromise or make arrangements with creditors and members.)

> (1) Where a compromise or arrangement is proposed— (a) between a company and its creditors or any class of them; or (b) between a company and its members or any class of them, the Tribunal may, on the application of the company or of any creditor or member of the company, or in the case of a company

```
question:
answer:
gold_clauses: ["s233(12)", "s230"]
anchor_clause: "s233(12)"
reference_path: [["s233(12)", "s230"]]
difficulty: one_hop
```

---

## 5. s66(3) -> s133

score 0.7321 | dissimilarity 0.9333 | target in-degree 7 | trigger `specified in`

**Anchor s66(3)** (Reduction of share capital.)

> The Tribunal may, if it is satisfied that the debt or claim of every creditor of the company has been discharged or determined or has been secured or his consent is obtained, make an order confirming the reduction of share capital on such terms and conditions as it deems fit: Provided that no applic

**Target s133** (Central Government to prescribe accounting standards.)

> The Central Government may prescribe the standards of accounting or any addendum thereto, as recommended by the Institute of Chartered Accountants of India, constituted under section 3 of the Chartered Accountants Act, 1949 (38 of 1949), in consultation with and after examination of the recommendati

```
question:
answer:
gold_clauses: ["s66(3)", "s133"]
anchor_clause: "s66(3)"
reference_path: [["s66(3)", "s133"]]
difficulty: one_hop
```

---

## 6. s183(1) -> s180

score 0.7321 | dissimilarity 0.9381 | target in-degree 1 | trigger `notwithstanding anything contained in`

**Anchor s183(1)** (Power of Board and other persons to make contributions to national defence fund, etc.)

> The Board of Directors of any company or any person or authority exercising the powers of the Board of Directors of a company, or of the company in general meeting, may, notwithstanding anything contained in sections 180, 181 and section 182 or any other provision of this Act or in the memorandum, a

**Target s180** (Restriction on powers of Board.)

> (1) The Board of Directors of a company shall exercise the following powers only with the consent of the company by a special resolution, namely:— (a) to sell, lease or otherwise dispose of the whole or substantially the whole of the undertaking of the company or where the company owns more than one

```
question:
answer:
gold_clauses: ["s183(1)", "s180"]
anchor_clause: "s183(1)"
reference_path: [["s183(1)", "s180"]]
difficulty: one_hop
```

---

## 7. s466(1) -> s465

score 0.7265 | dissimilarity 0.8648 | target in-degree 3 | trigger `notwithstanding anything contained in`

**Anchor s466(1)** (Dissolution of Company Law Board and consequential provisions.)

> Notwithstanding anything contained in section 465, the Board of Company Law Administration constituted under the Companies Act, 1956 (1 of 1956) (hereafter in this section referred to as the Company Law Board) shall stand dissolved on the constitution of the Tribunal and the Appellate Tribunal: Prov

**Target s465** (Repeal of certain enactments and savings.)

> (1) The Companies Act, 1956 (1 of 1956) and the Registration of Companies (Sikkim) Act, 1961 (Sikkim Act 8 of 1961) (hereafter in this section referred to as the repealed enactments) shall stand repealed: Provided that the provisions of Part IX A of the Companies Act, 1956 (1 of 1956) shall be appli

```
question:
answer:
gold_clauses: ["s466(1)", "s465"]
anchor_clause: "s466(1)"
reference_path: [["s466(1)", "s465"]]
difficulty: one_hop
```

---

## 8. s196(4) -> s197

score 0.7245 | dissimilarity 0.8793 | target in-degree 4 | trigger `subject to the provisions of`

**Anchor s196(4)** (Appointment of managing director, whole-time director or manager.)

> Subject to the provisions of section 197 and Schedule V, a managing director, whole-time director or manager shall be appointed and the terms and conditions of such appointment and remuneration payable be approved by the Board of Directors at a meeting which shall be subject to approval by a resolut

**Target s197** (Overall maximum managerial remuneration and managerial remuneration in case of absence or inadequacy of profits.)

> (1) The total managerial remuneration payable by a public company, to its directors, including managing director and whole-time director, and its manager in respect of any financial year shall not exceed eleven per cent. of the net profits of that company for that financial year computed in the mann

```
question:
answer:
gold_clauses: ["s196(4)", "s197"]
anchor_clause: "s196(4)"
reference_path: [["s196(4)", "s197"]]
difficulty: one_hop
```

---

## 9. s149(10) -> s152

score 0.7135 | dissimilarity 0.925 | target in-degree 2 | trigger `subject to the provisions of`

**Anchor s149(10)** (Company to have Board of Directors.)

> Subject to the provisions of section 152, an independent director shall hold office for a term up to five consecutive years on the Board of a company, but shall be eligible for reappointment on passing of a special resolution by the company and disclosure of such appointment in the Board’s report.

**Target s152** (Appointment of directors.)

> (1) Where no provision is made in the articles of a company for the appointment of the first director, the subscribers to the memorandum who are individuals shall be deemed to be the first directors of the company until the directors are duly appointed and in case of a One Person Company an individu

```
question:
answer:
gold_clauses: ["s149(10)", "s152"]
anchor_clause: "s149(10)"
reference_path: [["s149(10)", "s152"]]
difficulty: one_hop
```

---

## 10. s183(1) -> s181

score 0.7121 | dissimilarity 0.8727 | target in-degree 2 | trigger `notwithstanding anything contained in`

**Anchor s183(1)** (Power of Board and other persons to make contributions to national defence fund, etc.)

> The Board of Directors of any company or any person or authority exercising the powers of the Board of Directors of a company, or of the company in general meeting, may, notwithstanding anything contained in sections 180, 181 and section 182 or any other provision of this Act or in the memorandum, a

**Target s181** (Company to contribute to bona fide and charitable funds, etc.)

> The Board of Directors of a company may contribute to bona fide charitable and other funds: Provided that prior permission of the company in general meeting shall be required for such contribution in case any amount the aggregate of which, in any financial year, exceed five per cent. of its average 

```
question:
answer:
gold_clauses: ["s183(1)", "s181"]
anchor_clause: "s183(1)"
reference_path: [["s183(1)", "s181"]]
difficulty: one_hop
```

---

## 11. s54(1) -> s53

score 0.7026 | dissimilarity 0.8889 | target in-degree 1 | trigger `notwithstanding anything contained in`

**Anchor s54(1)** (Issue of sweat equity shares.)

> Notwithstanding anything contained in section 53, a company may issue sweat equity shares of a class of shares already issued, if the following conditions are fulfilled, namely:— (a) the issue is authorised by a special resolution passed by the company; (b) the resolution specifies the number of sha

**Target s53** (Prohibition on issue of shares at discount.)

> (1) Except as provided in section 54, a company shall not issue shares at a discount. (2) Any share issued by a company at a discounted price shall be void. (3) Where a company contravenes the provisions of this section, the company shall be punishable with fine which shall not be less than one lakh

```
question:
answer:
gold_clauses: ["s54(1)", "s53"]
anchor_clause: "s54(1)"
reference_path: [["s54(1)", "s53"]]
difficulty: one_hop
```

---

## 12. s147(1) -> s139

score 0.6908 | dissimilarity 0.966 | target in-degree 5 | trigger `none`

**Anchor s147(1)** (Punishment for contravention.)

> If any of the provisions of sections 139 to 146 (both inclusive) is contravened, the company shall be punishable with fine which shall not be less than twenty-five thousand rupees but which may extend to five lakh rupees and every officer of the company who is in default shall be punishable with imp

**Target s139** (Appointment of auditors.)

> (1) Subject to the provisions of this Chapter, every company shall, at the first annual general meeting, appoint an individual or a firm as an auditor who shall hold office from the conclusion of that meeting till the conclusion of its sixth annual general meeting and thereafter till the conclusion 

```
question:
answer:
gold_clauses: ["s147(1)", "s139"]
anchor_clause: "s147(1)"
reference_path: [["s147(1)", "s139"]]
difficulty: one_hop
```

---

## 13. s230(10) -> s68

score 0.6905 | dissimilarity 0.9655 | target in-degree 5 | trigger `none`

**Anchor s230(10)** (Power to compromise or make arrangements with creditors and members.)

> No compromise or arrangement in respect of any buy-back of securities under this section shall be sanctioned by the Tribunal unless such buy-back is in accordance with the provisions of section 68.

**Target s68** (Power of company to purchase its own securities.)

> (1) Notwithstanding anything contained in this Act, but subject to the provisions of sub-section (2), a company may purchase its own shares or other specified securities (hereinafter referred to as buy-back) out of— (a) its free reserves; (b) the securities premium account; or (c) the proceeds of th

```
question:
answer:
gold_clauses: ["s230(10)", "s68"]
anchor_clause: "s230(10)"
reference_path: [["s230(10)", "s68"]]
difficulty: one_hop
```

---

## 14. s233(5) -> s232

score 0.6831 | dissimilarity 0.9532 | target in-degree 5 | trigger `under`

**Anchor s233(5)** (Merger or amalgamation of certain companies.)

> If the Central Government after receiving the objections or suggestions or for any reason is of the opinion that such a scheme is not in public interest or in the interest of the creditors, it may file an application before the Tribunal within a period of sixty days of the receipt of the scheme unde

**Target s232** (Merger and amalgamation of companies.)

> (1) Where an application is made to the Tribunal under section 230 for the sanctioning of a compromise or an arrangement proposed between a company and any such persons as are mentioned in that section, and it is shown to the Tribunal— (a) that the compromise or arrangement has been proposed for the

```
question:
answer:
gold_clauses: ["s233(5)", "s232"]
anchor_clause: "s233(5)"
reference_path: [["s233(5)", "s232"]]
difficulty: one_hop
```

---

## 15. s249(1) -> s248(2)

score 0.6817 | dissimilarity 0.951 | target in-degree 5 | trigger `under`

**Anchor s249(1)** (Restrictions on making application under section 248 in certain situations.)

> An application under sub-section (2) of section 248 on behalf of a company shall not be made if, at any time in the previous three months, the company— (a) has changed its name or shifted its registered office from one State to another; (b) has made a disposal for value of property or rights held by

**Target s248(2)** (Power of Registrar to remove name of company from register of companies.)

> Without prejudice to the provisions of sub-section (1), a company may, after extinguishing all its liabilities, by a special resolution or consent of seventy-five per cent. members in terms of paid-up share capital, file an application in the prescribed manner to the Registrar for removing the name 

```
question:
answer:
gold_clauses: ["s249(1)", "s248(2)"]
anchor_clause: "s249(1)"
reference_path: [["s249(1)", "s248(2)"]]
difficulty: one_hop
```

---

## 16. s13(2) -> s4(2)

score 0.6767 | dissimilarity 0.8958 | target in-degree 1 | trigger `subject to the provisions of`

**Anchor s13(2)** (Alteration of memorandum.)

> Any change in the name of a company shall be subject to the provisions of subsections (2) and (3) of section 4 and shall not have effect except with the approval of the Central Government in writing: Provided that no such approval shall be necessary where the only change in the name of the company i

**Target s4(2)** (Memorandum.)

> The name stated in the memorandum shall not— (a) be identical with or resemble too nearly to the name of an existing company registered under this Act or any previous company law; or (b) be such that its use by the company— (i) will constitute an offence under any law for the time being in force; or

```
question:
answer:
gold_clauses: ["s13(2)", "s4(2)"]
anchor_clause: "s13(2)"
reference_path: [["s13(2)", "s4(2)"]]
difficulty: one_hop
```

---

## 17. s42(1) -> s26

score 0.6764 | dissimilarity 0.9741 | target in-degree 4 | trigger `none`

**Anchor s42(1)** (Offer or invitation for subscription of securities on private placement.)

> Without prejudice to the provisions of section 26, a company may, subject to the provisions of this section, make private placement through issue of a private placement offer letter.

**Target s26** (Matters to be stated in prospectus.)

> (1) Every prospectus issued by or on behalf of a public company either with reference to its formation or subsequently, or by or on behalf of any person who is or has been engaged or interested in the formation of a public company, shall be dated and signed and shall— (a) state the following informa

```
question:
answer:
gold_clauses: ["s42(1)", "s26"]
anchor_clause: "s42(1)"
reference_path: [["s42(1)", "s26"]]
difficulty: one_hop
```

---

## 18. s224(2) -> s213

score 0.6743 | dissimilarity 0.9206 | target in-degree 4 | trigger `referred to in`

**Anchor s224(2)** (Actions to be taken in pursuance of inspector’s report.)

> If any company or other body corporate is liable to be wound up under this Act and it appears to the Central Government from any such report made under section 223 that it is expedient so to do by reason of any such circumstances as are referred to in section 213, the Central Government may, unless 

**Target s213** (Investigation into company’s affairs in other cases.)

> The Tribunal may,— (a) on an application made by— (i) not less than one hundred members or members holding not less than one-tenth of the total voting power, in the case of a company having a share capital; or (ii) not less than one-fifth of the persons on the company’s register of members, in the c

```
question:
answer:
gold_clauses: ["s224(2)", "s213"]
anchor_clause: "s224(2)"
reference_path: [["s224(2)", "s213"]]
difficulty: one_hop
```

---

## 19. s177(8) -> s134(3)

score 0.6714 | dissimilarity 0.9658 | target in-degree 4 | trigger `under`

**Anchor s177(8)** (Audit Committee.)

> The Board’s report under sub-section (3) of section 134 shall disclose the composition of an Audit Committee and where the Board had not accepted any recommendation of the Audit Committee, the same shall be disclosed in such report along with the reasons therefor.

**Target s134(3)** (Financial statement, Board’s report, etc.)

> There shall be attached to statements laid before a company in general meeting, a report by its Board of Directors, which shall include— (a) the extract of the annual return as provided under sub-section (3) of section 92; (b) number of meetings of the Board; (c) Directors’ Responsibility Statement;

```
question:
answer:
gold_clauses: ["s177(8)", "s134(3)"]
anchor_clause: "s177(8)"
reference_path: [["s177(8)", "s134(3)"]]
difficulty: one_hop
```

---

## 20. s70(2) -> s92

score 0.6662 | dissimilarity 0.9571 | target in-degree 4 | trigger `none`

**Anchor s70(2)** (Prohibition for buy-back in certain circumstances.)

> No company shall, directly or indirectly, purchase its own shares or other specified securities in case such company has not complied with the provisions of sections 92, 123, 127 and section 129.

**Target s92** (Annual return.)

> (1) Every company shall prepare a return (hereinafter referred to as the annual return) in the prescribed form containing the particulars as they stood on the close of the financial year regarding— (a) its registered office, principal business activities, particulars of its holding, subsidiary and a

```
question:
answer:
gold_clauses: ["s70(2)", "s92"]
anchor_clause: "s70(2)"
reference_path: [["s70(2)", "s92"]]
difficulty: one_hop
```

---

## 21. s327(1) -> s326

score 0.6662 | dissimilarity 0.8141 | target in-degree 3 | trigger `subject to the provisions of`

**Anchor s327(1)** (Preferential payments.)

> In a winding up, subject to the provisions of section 326, there shall be paid in priority to all other debts,— (a) all revenues, taxes, cesses and rates due from the company to the Central Government or a State Government or to a local authority at the relevant date, and having become due and payab

**Target s326** (Overriding preferential payments.)

> (1) Notwithstanding anything contained in this Act or any other law for the time being in force, in the winding up of a company,— (a) workmen’s dues; and (b) debts due to secured creditors to the extent such debts rank under clause (iii) of the proviso to subsection (1) of section 325 pari passu wit

```
question:
answer:
gold_clauses: ["s327(1)", "s326"]
anchor_clause: "s327(1)"
reference_path: [["s327(1)", "s326"]]
difficulty: one_hop
```

---

## 22. s218(1)(a) -> s210

score 0.6601 | dissimilarity 0.9149 | target in-degree 5 | trigger `under`

**Anchor s218(1)(a)** (Protection of employees during investigation.)

> during the course of any investigation of the affairs and other matters of or relating to a company, other body corporate or person under section 210, section 212, section 213 or section 219 or of the membership and other matters of or relating to a company, or the ownership of shares in or debentur

**Target s210** (Investigation into affairs of company.)

> (1) Where the Central Government is of the opinion, that it is necessary to investigate into the affairs of a company,— (a) on the receipt of a report of the Registrar or inspector under section 208; (b) on intimation of a special resolution passed by a company that the affairs of the company ought 

```
question:
answer:
gold_clauses: ["s218(1)(a)", "s210"]
anchor_clause: "s218(1)(a)"
reference_path: [["s218(1)(a)", "s210"]]
difficulty: one_hop
```

---

## 23. s218(1)(a) -> s212

score 0.6591 | dissimilarity 0.9774 | target in-degree 3 | trigger `none`

**Anchor s218(1)(a)** (Protection of employees during investigation.)

> during the course of any investigation of the affairs and other matters of or relating to a company, other body corporate or person under section 210, section 212, section 213 or section 219 or of the membership and other matters of or relating to a company, or the ownership of shares in or debentur

**Target s212** (Investigation into affairs of Company by Serious Fraud Investigation Office.)

> (1) Without prejudice to the provisions of section 210, where the Central Government is of the opinion, that it is necessary to investigate into the affairs of a company by the Serious Fraud Investigation Office— (a) on receipt of a report of the Registrar or inspector under section 208; (b) on inti

```
question:
answer:
gold_clauses: ["s218(1)(a)", "s212"]
anchor_clause: "s218(1)(a)"
reference_path: [["s218(1)(a)", "s212"]]
difficulty: one_hop
```

---

## 24. s76(1) -> s73

score 0.6577 | dissimilarity 0.7821 | target in-degree 2 | trigger `notwithstanding anything contained in`

**Anchor s76(1)** (Acceptance of deposits from public by certain companies.)

> Notwithstanding anything contained in section 73, a public company, having such net worth or turnover as may be prescribed, may accept deposits from persons other than its members subject to compliance with the requirements provided in sub-section (2) of section 73 and subject to such rules as the C

**Target s73** (Prohibition on acceptance of deposits from public.)

> (1) On and after the commencement of this Act, no company shall invite, accept or renew deposits under this Act from the public except in a manner provided under this Chapter: Provided that nothing in this sub-section shall apply to a banking company and nonbanking financial company as defined in th

```
question:
answer:
gold_clauses: ["s76(1)", "s73"]
anchor_clause: "s76(1)"
reference_path: [["s76(1)", "s73"]]
difficulty: one_hop
```

---

## 25. s13(2) -> s4(3)

score 0.655 | dissimilarity 0.8596 | target in-degree 1 | trigger `subject to the provisions of`

**Anchor s13(2)** (Alteration of memorandum.)

> Any change in the name of a company shall be subject to the provisions of subsections (2) and (3) of section 4 and shall not have effect except with the approval of the Central Government in writing: Provided that no such approval shall be necessary where the only change in the name of the company i

**Target s4(3)** (Memorandum.)

> Without prejudice to the provisions of sub-section (2), a company shall not be registered with a name which contains— (a) any word or expression which is likely to give the impression that the company is in any way connected with, or having the patronage of, the Central Government, any State Governm

```
question:
answer:
gold_clauses: ["s13(2)", "s4(3)"]
anchor_clause: "s13(2)"
reference_path: [["s13(2)", "s4(3)"]]
difficulty: one_hop
```

---

## 26. s47(1) -> s43

score 0.6544 | dissimilarity 0.8587 | target in-degree 1 | trigger `subject to the provisions of`

**Anchor s47(1)** (Voting rights.)

> Subject to the provisions of section 43 and sub-section (2) of section 50,— (a) every member of a company limited by shares and holding equity share capital therein, shall have a right to vote on every resolution placed before the company; and (b) his voting right on a poll shall be in proportion to

**Target s43** (Kinds of share capital.)

> The share capital of a company limited by shares shall be of two kinds, namely:— (a) equity share capital— (i) with voting rights; or (ii) with differential rights as to dividend, voting or otherwise in accordance with such rules as may be prescribed; and (b) preference share capital: Provided that 

```
question:
answer:
gold_clauses: ["s47(1)", "s43"]
anchor_clause: "s47(1)"
reference_path: [["s47(1)", "s43"]]
difficulty: one_hop
```

---

## 27. s70(2) -> s129

score 0.6529 | dissimilarity 0.967 | target in-degree 3 | trigger `none`

**Anchor s70(2)** (Prohibition for buy-back in certain circumstances.)

> No company shall, directly or indirectly, purchase its own shares or other specified securities in case such company has not complied with the provisions of sections 92, 123, 127 and section 129.

**Target s129** (Financial statement.)

> (1) The financial statements shall give a true and fair view of the state of affairs of the company or companies, comply with the accounting standards notified under section 133 and shall be in the form or forms as may be provided for different class or classes of companies in Schedule III: Provided

```
question:
answer:
gold_clauses: ["s70(2)", "s129"]
anchor_clause: "s70(2)"
reference_path: [["s70(2)", "s129"]]
difficulty: one_hop
```

---

## 28. s371(6) -> s242

score 0.6499 | dissimilarity 0.9621 | target in-degree 3 | trigger `none`

**Anchor s371(6)** (Effect of registration under this Part.)

> None of the provisions of this Act (apart from those of section 242) shall derogate from any power of altering its constitution or regulations which may be vested in the company, by virtue of any Act of Parliament or any other law for the time being in force, or other instrument constituting or regu

**Target s242** (Powers of Tribunal.)

> (1) If, on any application made under section 241, the Tribunal is of the opinion— (a) that the company’s affairs have been or are being conducted in a manner prejudicial or oppressive to any member or members or prejudicial to public interest or in a manner prejudicial to the interests of the compa

```
question:
answer:
gold_clauses: ["s371(6)", "s242"]
anchor_clause: "s371(6)"
reference_path: [["s371(6)", "s242"]]
difficulty: one_hop
```

---

## 29. s147(1) -> s144

score 0.6492 | dissimilarity 0.9608 | target in-degree 3 | trigger `none`

**Anchor s147(1)** (Punishment for contravention.)

> If any of the provisions of sections 139 to 146 (both inclusive) is contravened, the company shall be punishable with fine which shall not be less than twenty-five thousand rupees but which may extend to five lakh rupees and every officer of the company who is in default shall be punishable with imp

**Target s144** (Auditor not to render certain services.)

> An auditor appointed under this Act shall provide to the company only such other services as are approved by the Board of Directors or the audit committee, as the case may be, but which shall not include any of the following services (whether such services are rendered directly or indirectly to the 

```
question:
answer:
gold_clauses: ["s147(1)", "s144"]
anchor_clause: "s147(1)"
reference_path: [["s147(1)", "s144"]]
difficulty: one_hop
```

---

## 30. s147(1) -> s143

score 0.6465 | dissimilarity 0.9564 | target in-degree 3 | trigger `none`

**Anchor s147(1)** (Punishment for contravention.)

> If any of the provisions of sections 139 to 146 (both inclusive) is contravened, the company shall be punishable with fine which shall not be less than twenty-five thousand rupees but which may extend to five lakh rupees and every officer of the company who is in default shall be punishable with imp

**Target s143** (Powers and duties of auditors and auditing standards.)

> (1) Every auditor of a company shall have a right of access at all times to the books of account and vouchers of the company, whether kept at the registered office of the company or at any other place and shall be entitled to require from the officers of the company such information and explanation 

```
question:
answer:
gold_clauses: ["s147(1)", "s143"]
anchor_clause: "s147(1)"
reference_path: [["s147(1)", "s143"]]
difficulty: one_hop
```

---

## 31. s254(1) -> s13(4)

score 0.6448 | dissimilarity 0.9855 | target in-degree 2 | trigger `under`

**Anchor s254(1)** (Application for revival and rehabilitation.)

> On the determination of a company as a sick company by the Tribunal under section 253, any secured creditor of that company or the company may make an application to the Tribunal for the determination of the measures that may be adopted with respect to the revival and rehabilitation of such company:

**Target s13(4)** (Alteration of memorandum.)

> The alteration of the memorandum relating to the place of the registered office from one State to another shall not have any effect unless it is approved by the Central Government on an application in such form and manner as may be prescribed.

```
question:
answer:
gold_clauses: ["s254(1)", "s13(4)"]
anchor_clause: "s254(1)"
reference_path: [["s254(1)", "s13(4)"]]
difficulty: one_hop
```

---

## 32. s391(1) -> s36

score 0.6438 | dissimilarity 0.9839 | target in-degree 2 | trigger `none`

**Anchor s391(1)** (Application of sections 34 to 36 and Chapter XX.)

> The provisions of sections 34 to 36 (both inclusive) shall apply to— (i) the issue of a prospectus by a company incorporated outside India under section 389 as they apply to prospectus issued by an Indian company; (ii) the issue of Indian Depository Receipts by a foreign company.

**Target s36** (Punishment for fraudulently inducing persons to invest money.)

> Any person who, either knowingly or recklessly makes any statement, promise or forecast which is false, deceptive or misleading, or deliberately conceals any material facts, to induce another person to enter into, or to offer to enter into,— (a) any agreement for, or with a view to, acquiring, dispo

```
question:
answer:
gold_clauses: ["s391(1)", "s36"]
anchor_clause: "s391(1)"
reference_path: [["s391(1)", "s36"]]
difficulty: one_hop
```

---

## 33. s123(6) -> s74

score 0.641 | dissimilarity 0.9792 | target in-degree 2 | trigger `none`

**Anchor s123(6)** (Declaration of dividend.)

> A company which fails to comply with the provisions of sections 73 and 74 shall not, so long as such failure continues, declare any dividend on its equity shares.

**Target s74** (Repayment of deposits, etc., accepted before commencement of this Act.)

> (1) Where in respect of any deposit accepted by a company before the commencement of this Act, the amount of such deposit or part thereof or any interest due thereon remains unpaid on such commencement or becomes due at any time thereafter, the company shall— (a) file, within a period of three month

```
question:
answer:
gold_clauses: ["s123(6)", "s74"]
anchor_clause: "s123(6)"
reference_path: [["s123(6)", "s74"]]
difficulty: one_hop
```

---

## 34. s150(1) -> s149(6)

score 0.6371 | dissimilarity 0.9407 | target in-degree 3 | trigger `none`

**Anchor s150(1)** (Manner of selection of independent directors and maintenance of databank of independent directors.)

> Subject to the provisions contained in sub-section (6) of section 149, an independent director may be selected from a data bank containing names, addresses and qualifications of persons who are eligible and willing to act as independent directors, maintained by any body, institute or association, as

**Target s149(6)** (Company to have Board of Directors.)

> An independent director in relation to a company, means a director other than a managing director or a whole-time director or a nominee director,— (a) who, in the opinion of the Board, is a person of integrity and possesses relevant expertise and experience; (b) (i) who is or was not a promoter of t

```
question:
answer:
gold_clauses: ["s150(1)", "s149(6)"]
anchor_clause: "s150(1)"
reference_path: [["s150(1)", "s149(6)"]]
difficulty: one_hop
```

---

## 35. s164(1)(g) -> s188

score 0.6364 | dissimilarity 0.9716 | target in-degree 2 | trigger `under`

**Anchor s164(1)(g)** (Disqualifications for appointment of director.)

> he has been convicted of the offence dealing with related party transactions under section 188 at any time during the last preceding five years; or

**Target s188** (Related party transactions.)

> (1) Except with the consent of the Board of Directors given by a resolution at a meeting of the Board and subject to such conditions as may be prescribed, no company shall enter into any contract or arrangement with a related party with respect to— (a) sale, purchase or supply of any goods or materi

```
question:
answer:
gold_clauses: ["s164(1)(g)", "s188"]
anchor_clause: "s164(1)(g)"
reference_path: [["s164(1)(g)", "s188"]]
difficulty: one_hop
```

---

## 36. s70(2) -> s127

score 0.6318 | dissimilarity 0.9639 | target in-degree 2 | trigger `none`

**Anchor s70(2)** (Prohibition for buy-back in certain circumstances.)

> No company shall, directly or indirectly, purchase its own shares or other specified securities in case such company has not complied with the provisions of sections 92, 123, 127 and section 129.

**Target s127** (Punishment for failure to distribute dividends.)

> Where a dividend has been declared by a company but has not been paid or the warrant in respect thereof has not been posted within thirty days from the date of declaration to any shareholder entitled to the payment of the dividend, every director of the company shall, if he is knowingly a party to t

```
question:
answer:
gold_clauses: ["s70(2)", "s127"]
anchor_clause: "s70(2)"
reference_path: [["s70(2)", "s127"]]
difficulty: one_hop
```

---

## 37. s147(1) -> s145

score 0.6295 | dissimilarity 0.96 | target in-degree 2 | trigger `none`

**Anchor s147(1)** (Punishment for contravention.)

> If any of the provisions of sections 139 to 146 (both inclusive) is contravened, the company shall be punishable with fine which shall not be less than twenty-five thousand rupees but which may extend to five lakh rupees and every officer of the company who is in default shall be punishable with imp

**Target s145** (Auditor to sign audit reports, etc.)

> The person appointed as an auditor of the company shall sign the auditor’s report or sign or certify any other document of the company in accordance with the provisions of sub-section (2) of section 141, and the qualifications, observations or comments on financial transactions or matters, which hav

```
question:
answer:
gold_clauses: ["s147(1)", "s145"]
anchor_clause: "s147(1)"
reference_path: [["s147(1)", "s145"]]
difficulty: one_hop
```

---

## 38. s70(2) -> s123

score 0.6272 | dissimilarity 0.9562 | target in-degree 2 | trigger `none`

**Anchor s70(2)** (Prohibition for buy-back in certain circumstances.)

> No company shall, directly or indirectly, purchase its own shares or other specified securities in case such company has not complied with the provisions of sections 92, 123, 127 and section 129.

**Target s123** (Declaration of dividend.)

> (1) No dividend shall be declared or paid by a company for any financial year except— (a) out of the profits of the company for that year arrived at after providing for depreciation in accordance with the provisions of sub-section (2), or out of the profits of the company for any previous financial 

```
question:
answer:
gold_clauses: ["s70(2)", "s123"]
anchor_clause: "s70(2)"
reference_path: [["s70(2)", "s123"]]
difficulty: one_hop
```

---

## 39. s2(70) -> s31

score 0.6271 | dissimilarity 0.9381 | target in-degree 1 | trigger `referred to in`

**Anchor s2(70)** (Definitions.)

> “prospectus” means any document described or issued as a prospectus and includes a red herring prospectus referred to in section 32 or shelf prospectus referred to in section 31 or any notice, circular, advertisement or other document inviting offers from the public for the subscription or purchase 

**Target s31** (Shelf prospectus.)

> (1) Any class or classes of companies, as the Securities and Exchange Board may provide by regulations in this behalf, may file a shelf prospectus with the Registrar at the stage of the first offer of securities included therein which shall indicate a period not exceeding one year as the period of v

```
question:
answer:
gold_clauses: ["s2(70)", "s31"]
anchor_clause: "s2(70)"
reference_path: [["s2(70)", "s31"]]
difficulty: one_hop
```

---

## 40. s139(11) -> s177

score 0.6265 | dissimilarity 0.9551 | target in-degree 2 | trigger `under`

**Anchor s139(11)** (Appointment of auditors.)

> Where a company is required to constitute an Audit Committee under section 177, all appointments, including the filling of a casual vacancy of an auditor under this section shall be made after taking into account the recommendations of such committee.

**Target s177** (Audit Committee.)

> (1) The Board of Directors of every listed company and such other class or classes of companies, as may be prescribed, shall constitute an Audit Committee. (2) The Audit Committee shall consist of a minimum of three directors with independent directors forming a majority: Provided that majority of m

```
question:
answer:
gold_clauses: ["s139(11)", "s177"]
anchor_clause: "s139(11)"
reference_path: [["s139(11)", "s177"]]
difficulty: one_hop
```

---

## 41. s111(1) -> s100

score 0.6255 | dissimilarity 0.9213 | target in-degree 3 | trigger `none`

**Anchor s111(1)** (Circulation of members’ resolution.)

> A company shall, on requisition in writing of such number of members, as required in section 100,— (a) give notice to members of any resolution which may properly be moved and is intended to be moved at a meeting; and (b) circulate to members any statement with respect to the matters referred to in 

**Target s100** (Calling of extraordinary general meeting.)

> (1) The Board may, whenever it deems fit, call an extraordinary general meeting of the company. (2) The Board shall, at the requisition made by,— (a) in the case of a company having a share capital, such number of members who hold, on the date of the receipt of the requisition, not less than one-ten

```
question:
answer:
gold_clauses: ["s111(1)", "s100"]
anchor_clause: "s111(1)"
reference_path: [["s111(1)", "s100"]]
difficulty: one_hop
```

---

## 42. s254(1) -> s5(1)

score 0.6235 | dissimilarity 0.9821 | target in-degree 1 | trigger `under`

**Anchor s254(1)** (Application for revival and rehabilitation.)

> On the determination of a company as a sick company by the Tribunal under section 253, any secured creditor of that company or the company may make an application to the Tribunal for the determination of the measures that may be adopted with respect to the revival and rehabilitation of such company:

**Target s5(1)** (Articles.)

> The articles of a company shall contain the regulations for management of the company.

```
question:
answer:
gold_clauses: ["s254(1)", "s5(1)"]
anchor_clause: "s254(1)"
reference_path: [["s254(1)", "s5(1)"]]
difficulty: one_hop
```

---

## 43. s147(1) -> s142

score 0.6229 | dissimilarity 0.9811 | target in-degree 1 | trigger `none`

**Anchor s147(1)** (Punishment for contravention.)

> If any of the provisions of sections 139 to 146 (both inclusive) is contravened, the company shall be punishable with fine which shall not be less than twenty-five thousand rupees but which may extend to five lakh rupees and every officer of the company who is in default shall be punishable with imp

**Target s142** (Remuneration of auditors.)

> (1) The remuneration of the auditor of a company shall be fixed in its general meeting or in such manner as may be determined therein: Provided that the Board may fix remuneration of the first auditor appointed by it. (2) The remuneration under sub-section (1) shall, in addition to the fee payable t

```
question:
answer:
gold_clauses: ["s147(1)", "s142"]
anchor_clause: "s147(1)"
reference_path: [["s147(1)", "s142"]]
difficulty: one_hop
```

---

## 44. s147(1) -> s146

score 0.6217 | dissimilarity 0.9792 | target in-degree 1 | trigger `none`

**Anchor s147(1)** (Punishment for contravention.)

> If any of the provisions of sections 139 to 146 (both inclusive) is contravened, the company shall be punishable with fine which shall not be less than twenty-five thousand rupees but which may extend to five lakh rupees and every officer of the company who is in default shall be punishable with imp

**Target s146** (Auditors to attend general meeting.)

> All notices of, and other communications relating to, any general meeting shall be forwarded to the auditor of the company, and the auditor shall, unless otherwise exempted by the company, attend either by himself or through his authorised representative, who shall also be qualified to be an auditor

```
question:
answer:
gold_clauses: ["s147(1)", "s146"]
anchor_clause: "s147(1)"
reference_path: [["s147(1)", "s146"]]
difficulty: one_hop
```

---

## 45. s147(1) -> s141

score 0.6201 | dissimilarity 0.9444 | target in-degree 2 | trigger `none`

**Anchor s147(1)** (Punishment for contravention.)

> If any of the provisions of sections 139 to 146 (both inclusive) is contravened, the company shall be punishable with fine which shall not be less than twenty-five thousand rupees but which may extend to five lakh rupees and every officer of the company who is in default shall be punishable with imp

**Target s141** (Eligibility, qualifications and disqualifications of auditors.)

> (1) A person shall be eligible for appointment as an auditor of a company only if he is a chartered accountant: Provided that a firm whereof majority of partners practising in India are qualified for appointment as aforesaid may be appointed by its firm name to be auditor of a company. (2) Where a f

```
question:
answer:
gold_clauses: ["s147(1)", "s141"]
anchor_clause: "s147(1)"
reference_path: [["s147(1)", "s141"]]
difficulty: one_hop
```

---

## 46. s124(5) -> s125(1)

score 0.6199 | dissimilarity 0.9762 | target in-degree 1 | trigger `under`

**Anchor s124(5)** (Unpaid Dividend Account.)

> Any money transferred to the Unpaid Dividend Account of a company in pursuance of this section which remains unpaid or unclaimed for a period of seven years from the date of such transfer shall be transferred by the company along with interest accrued, if any, thereon to the Fund established under s

**Target s125(1)** (Investor Education and Protection Fund.)

> The Central Government shall establish a Fund to be called the Investor Education and Protection Fund (herein referred to as the Fund).

```
question:
answer:
gold_clauses: ["s124(5)", "s125(1)"]
anchor_clause: "s124(5)"
reference_path: [["s124(5)", "s125(1)"]]
difficulty: one_hop
```

---

## 47. s125(3)(d) -> s245

score 0.6198 | dissimilarity 0.976 | target in-degree 1 | trigger `under`

**Anchor s125(3)(d)** (Investor Education and Protection Fund.)

> reimbursement of legal expenses incurred in pursuing class action suits under sections 37 and 245 by members, debenture-holders or depositors as may be sanctioned by the Tribunal; and

**Target s245** (Class action.)

> (1) Such number of member or members, depositor or depositors or any class of them, as the case may be, as are indicated in sub-section (2) may, if they are of the opinion that the management or conduct of the affairs of the company are being conducted in a manner prejudicial to the interests of the

```
question:
answer:
gold_clauses: ["s125(3)(d)", "s245"]
anchor_clause: "s125(3)(d)"
reference_path: [["s125(3)(d)", "s245"]]
difficulty: one_hop
```

---

## 48. s68(8) -> s62(1)(a)

score 0.6185 | dissimilarity 0.9417 | target in-degree 2 | trigger `under`

**Anchor s68(8)** (Power of company to purchase its own securities.)

> Where a company completes a buy-back of its shares or other specified securities under this section, it shall not make a further issue of the same kind of shares or other securities including allotment of new shares under clause (a) of sub-section (1) of section 62 or other specified securities with

**Target s62(1)(a)** (Further issue of share capital.)

> to persons who, at the date of the offer, are holders of equity shares of the company in proportion, as nearly as circumstances admit, to the paid-up share capital on those shares by sending a letter of offer subject to the following conditions, namely:— (i) the offer shall be made by notice specify

```
question:
answer:
gold_clauses: ["s68(8)", "s62(1)(a)"]
anchor_clause: "s68(8)"
reference_path: [["s68(8)", "s62(1)(a)"]]
difficulty: one_hop
```

---

## 49. s117(3)(e) -> s180(1)(c)

score 0.616 | dissimilarity 0.9697 | target in-degree 1 | trigger `none`

**Anchor s117(3)(e)** (Resolutions and agreements to be filed.)

> resolutions passed by a company according consent to the exercise by its Board of Directors of any of the powers under clause (a) and clause (c) of sub-section (1) of section 180;

**Target s180(1)(c)** (Restriction on powers of Board.)

> to borrow money, where the money to be borrowed, together with the money already borrowed by the company will exceed aggregate of its paid-up share capital and free reserves, apart from temporary loans obtained from the company’s bankers in the ordinary course of business:

```
question:
answer:
gold_clauses: ["s117(3)(e)", "s180(1)(c)"]
anchor_clause: "s117(3)(e)"
reference_path: [["s117(3)(e)", "s180(1)(c)"]]
difficulty: one_hop
```

---

## 50. s167(1)(c) -> s184

score 0.6156 | dissimilarity 0.9369 | target in-degree 2 | trigger `none`

**Anchor s167(1)(c)** (Vacation of office of director.)

> he acts in contravention of the provisions of section 184 relating to entering into contracts or arrangements in which he is directly or indirectly interested;

**Target s184** (Disclosure of interest by director.)

> (1) Every director shall at the first meeting of the Board in which he participates as a director and thereafter at the first meeting of the Board in every financial year or whenever there is any change in the disclosures already made, then at the first Board meeting held after such change, disclose

```
question:
answer:
gold_clauses: ["s167(1)(c)", "s184"]
anchor_clause: "s167(1)(c)"
reference_path: [["s167(1)(c)", "s184"]]
difficulty: one_hop
```

---

## 51. s125(3)(d) -> s37

score 0.6142 | dissimilarity 0.9667 | target in-degree 1 | trigger `under`

**Anchor s125(3)(d)** (Investor Education and Protection Fund.)

> reimbursement of legal expenses incurred in pursuing class action suits under sections 37 and 245 by members, debenture-holders or depositors as may be sanctioned by the Tribunal; and

**Target s37** (Action by affected persons.)

> A suit may be filed or any other action may be taken under section 34 or section 35 or section 36 by any person, group of persons or any association of persons affected by any misleading statement or the inclusion or omission of any matter in the prospectus.

```
question:
answer:
gold_clauses: ["s125(3)(d)", "s37"]
anchor_clause: "s125(3)(d)"
reference_path: [["s125(3)(d)", "s37"]]
difficulty: one_hop
```

---

## 52. s150(4) -> s149

score 0.6118 | dissimilarity 0.9627 | target in-degree 1 | trigger `under`

**Anchor s150(4)** (Manner of selection of independent directors and maintenance of databank of independent directors.)

> The Central Government may prescribe the manner and procedure of selection of independent directors who fulfil the qualifications and requirements specified under section 149.

**Target s149** (Company to have Board of Directors.)

> (1) Every company shall have a Board of Directors consisting of individuals as directors and shall have— (a) a minimum number of three directors in the case of a public company, two directors in the case of a private company, and one director in the case of a One Person Company; and (b) a maximum of

```
question:
answer:
gold_clauses: ["s150(4)", "s149"]
anchor_clause: "s150(4)"
reference_path: [["s150(4)", "s149"]]
difficulty: one_hop
```

---

## 53. s225(1)(a) -> s224

score 0.6096 | dissimilarity 0.9268 | target in-degree 2 | trigger `under`

**Anchor s225(1)(a)** (Expenses of investigation.)

> any person who is convicted on a prosecution instituted, or who is ordered to pay damages or restore any property in proceedings brought, under section 224, to the extent that he may in the same proceedings be ordered to pay the said expenses as may be specified by the court convicting such person, 

**Target s224** (Actions to be taken in pursuance of inspector’s report.)

> (1) If, from an inspector’s report, made under section 223, it appears to the Central Government that any person has, in relation to the company or in relation to any other body corporate or other person whose affairs have been investigated under this Chapter been guilty of any offence for which he 

```
question:
answer:
gold_clauses: ["s225(1)(a)", "s224"]
anchor_clause: "s225(1)(a)"
reference_path: [["s225(1)(a)", "s224"]]
difficulty: one_hop
```

---

## 54. s254(3) -> s253

score 0.6087 | dissimilarity 0.9255 | target in-degree 2 | trigger `under`

**Anchor s254(3)** (Application for revival and rehabilitation.)

> An application under sub-section (1) shall be made to the Tribunal within a period of sixty days from the date of determination of the company as a sick company by the Tribunal under section 253.

**Target s253** (Determination of sickness.)

> (1) Where on a demand by the secured creditors of a company representing fifty per cent. or more of its outstanding amount of debt, the company has failed to pay the debt within a period of thirty days of the service of the notice of demand or to secure or compound it to the reasonable satisfaction 

```
question:
answer:
gold_clauses: ["s254(3)", "s253"]
anchor_clause: "s254(3)"
reference_path: [["s254(3)", "s253"]]
difficulty: one_hop
```

---

## 55. s261(1) -> s254

score 0.6084 | dissimilarity 0.8929 | target in-degree 3 | trigger `under`

**Anchor s261(1)** (Scheme of revival and rehabilitation.)

> The company administrator shall prepare or cause to be prepared a scheme of revival and rehabilitation of the sick company after considering the draft scheme filed along with the application under section 254.

**Target s254** (Application for revival and rehabilitation.)

> (1) On the determination of a company as a sick company by the Tribunal under section 253, any secured creditor of that company or the company may make an application to the Tribunal for the determination of the measures that may be adopted with respect to the revival and rehabilitation of such comp

```
question:
answer:
gold_clauses: ["s261(1)", "s254"]
anchor_clause: "s261(1)"
reference_path: [["s261(1)", "s254"]]
difficulty: one_hop
```

---

## 56. s222(1) -> s216

score 0.608 | dissimilarity 0.8922 | target in-degree 3 | trigger `under`

**Anchor s222(1)** (Imposition of restrictions upon securities.)

> Where it appears to the Tribunal, in connection with any investigation under section 216 or on a complaint made by any person in this behalf, that there is good reason to find out the relevant facts about any securities issued or to be issued by a company and the Tribunal is of the opinion that such

**Target s216** (Investigation of ownership of company.)

> (1) Where it appears to the Central Government that there is a reason so to do, it may appoint one or more inspectors to investigate and report on matters relating to the company, and its membership for the purpose of determining the true persons— (a) who are or have been financially interested in t

```
question:
answer:
gold_clauses: ["s222(1)", "s216"]
anchor_clause: "s222(1)"
reference_path: [["s222(1)", "s216"]]
difficulty: one_hop
```

---

## 57. s306(1) -> s304

score 0.6048 | dissimilarity 0.9189 | target in-degree 2 | trigger `under`

**Anchor s306(1)** (Meeting of creditors.)

> The company shall along with the calling of meeting of the company at which the resolution for the voluntary winding up is to be proposed, cause a meeting of its creditors either on the same day or on the next day and shall cause a notice of such meeting to be sent by registered post to the creditor

**Target s304** (Circumstances in which company may be wound up voluntarily.)

> A company may be wound up voluntarily,— (a) if the company in general meeting passes a resolution requiring the company to be wound up voluntarily as a result of the expiry of the period for its duration, if any, fixed by its articles or on the occurrence of any event in respect of which the article

```
question:
answer:
gold_clauses: ["s306(1)", "s304"]
anchor_clause: "s306(1)"
reference_path: [["s306(1)", "s304"]]
difficulty: one_hop
```

---

## 58. s212(4) -> s217

score 0.6047 | dissimilarity 0.9508 | target in-degree 1 | trigger `under`

**Anchor s212(4)** (Investigation into affairs of Company by Serious Fraud Investigation Office.)

> The Director, Serious Fraud Investigation Office shall cause the affairs of the company to be investigated by an Investigating Officer who shall have the power of the inspector under section 217.

**Target s217** (Procedure, powers, etc., of inspectors.)

> (1) It shall be the duty of all officers and other employees and agents including the former officers, employees and agents of a company which is under investigation in accordance with the provisions contained in this Chapter, and where the affairs of any other body corporate or a person are investi

```
question:
answer:
gold_clauses: ["s212(4)", "s217"]
anchor_clause: "s212(4)"
reference_path: [["s212(4)", "s217"]]
difficulty: one_hop
```

---

## 59. s232(1) -> s230(5)

score 0.6045 | dissimilarity 0.9505 | target in-degree 1 | trigger `none`

**Anchor s232(1)** (Merger and amalgamation of companies.)

> Where an application is made to the Tribunal under section 230 for the sanctioning of a compromise or an arrangement proposed between a company and any such persons as are mentioned in that section, and it is shown to the Tribunal— (a) that the compromise or arrangement has been proposed for the pur

**Target s230(5)** (Power to compromise or make arrangements with creditors and members.)

> A notice under sub-section (3) along with all the documents in such form as may be prescribed shall also be sent to the Central Government, the income-tax authorities, the Reserve Bank of India, the Securities and Exchange Board, the Registrar, the respective stock exchanges, the Official Liquidator

```
question:
answer:
gold_clauses: ["s232(1)", "s230(5)"]
anchor_clause: "s232(1)"
reference_path: [["s232(1)", "s230(5)"]]
difficulty: one_hop
```

---

## 60. s131(1) -> s134

score 0.6041 | dissimilarity 0.9178 | target in-degree 2 | trigger `none`

**Anchor s131(1)** (Voluntary revision of financial statements or Board’s report.)

> If it appears to the directors of a company that— (a) the financial statement of the company; or (b) the report of the Board, do not comply with the provisions of section 129 or section 134 they may prepare revised financial statement or a revised report in respect of any of the three preceding fina

**Target s134** (Financial statement, Board’s report, etc.)

> (1) The financial statement, including consolidated financial statement, if any, shall be approved by the Board of Directors before they are signed on behalf of the Board at least by the chairperson of the company where he is authorised by the Board or by two directors out of which one shall be mana

```
question:
answer:
gold_clauses: ["s131(1)", "s134"]
anchor_clause: "s131(1)"
reference_path: [["s131(1)", "s134"]]
difficulty: one_hop
```

---

## 61. s117(1) -> s102

score 0.6038 | dissimilarity 0.9172 | target in-degree 2 | trigger `under`

**Anchor s117(1)** (Resolutions and agreements to be filed.)

> A copy of every resolution or any agreement, in respect of matters specified in sub-section (3) together with the explanatory statement under section 102, if any, annexed to the notice calling the meeting in which the resolution is proposed, shall be filed with the Registrar within thirty days of th

**Target s102** (Statement to be annexed to notice.)

> (1) A statement setting out the following material facts concerning each item of special business to be transacted at a general meeting, shall be annexed to the notice calling such meeting, namely:— (a) the nature of concern or interest, financial or otherwise, if any, in respect of each items of— (

```
question:
answer:
gold_clauses: ["s117(1)", "s102"]
anchor_clause: "s117(1)"
reference_path: [["s117(1)", "s102"]]
difficulty: one_hop
```

---

## 62. s311(4) -> s310

score 0.6035 | dissimilarity 0.9167 | target in-degree 2 | trigger `under`

**Anchor s311(4)** (Power to remove and fill vacancy of Company Liquidator.)

> If a vacancy occurs by death, resignation, removal or otherwise in the office of any Company Liquidator appointed under section 310, the company or the creditors, as the case may be, fill the vacancy in the manner specified in that section.

**Target s310** (Appointment of Company Liquidator.)

> (1) The company in its general meeting, where a resolution of voluntary winding up is passed, shall appoint a Company Liquidator from the panel prepared by the Central Government for the purpose of winding up its affairs and distributing the assets of the company and recommend the fee to be paid to 

```
question:
answer:
gold_clauses: ["s311(4)", "s310"]
anchor_clause: "s311(4)"
reference_path: [["s311(4)", "s310"]]
difficulty: one_hop
```

---

## 63. s244(1) -> s241

score 0.6032 | dissimilarity 0.8842 | target in-degree 3 | trigger `under`

**Anchor s244(1)** (Right to apply under section 241.)

> The following members of a company shall have the right to apply under section 241, namely:— (a) in the case of a company having a share capital, not less than one hundred members of the company or not less than one-tenth of the total number of its members, whichever is less, or any member or member

**Target s241** (Application to Tribunal for relief in cases of oppression, etc.)

> (1) Any member of a company who complains that— (a) the affairs of the company have been or are being conducted in a manner prejudicial to public interest or in a manner prejudicial or oppressive to him or any other member or members or in a manner prejudicial to the interests of the company; or (b)

```
question:
answer:
gold_clauses: ["s244(1)", "s241"]
anchor_clause: "s244(1)"
reference_path: [["s244(1)", "s241"]]
difficulty: one_hop
```

---

## 64. s122(3) -> s118

score 0.6031 | dissimilarity 0.9161 | target in-degree 2 | trigger `under`

**Anchor s122(3)** (Applicability of this Chapter to One Person Company.)

> For the purposes of section 114, any business which is required to be transacted at an annual general meeting or other general meeting of a company by means of an ordinary or special resolution, it shall be sufficient if, in case of One Person Company, the resolution is communicated by the member to

**Target s118** (Minutes of proceedings of general meeting, meeting of Board of Directors and other meeting and resolutions passed by postal ballot.)

> (1) Every company shall cause minutes of the proceedings of every general meeting of any class of shareholders or creditors, and every resolution passed by postal ballot and every meeting of its Board of Directors or of every committee of the Board, to be prepared and signed in such manner as may be

```
question:
answer:
gold_clauses: ["s122(3)", "s118"]
anchor_clause: "s122(3)"
reference_path: [["s122(3)", "s118"]]
difficulty: one_hop
```

---

## 65. s207(2) -> s206

score 0.6031 | dissimilarity 0.9161 | target in-degree 2 | trigger `under`

**Anchor s207(2)** (Conduct of inspection and inquiry.)

> The Registrar or inspector, making an inspection or inquiry under section 206 may, during the course of such inspection or inquiry, as the case may be,— (a) make or cause to be made copies of books of account and other books and papers; or (b) place or cause to be placed any marks of identification 

**Target s206** (Power to call for information, inspect books and conduct inquiries.)

> (1) Where on a scrutiny of any document filed by a company or on any information received by him, the Registrar is of the opinion that any further information or explanation or any further documents relating to the company is necessary, he may by a written notice require the company— (a) to furnish 

```
question:
answer:
gold_clauses: ["s207(2)", "s206"]
anchor_clause: "s207(2)"
reference_path: [["s207(2)", "s206"]]
difficulty: one_hop
```

---

## 66. s205(2) -> s204

score 0.6026 | dissimilarity 0.9153 | target in-degree 2 | trigger `none`

**Anchor s205(2)** (Functions of company secretary.)

> The provisions contained in section 204 and section 205 shall not affect the duties and functions of the Board of Directors, chairperson of the company, managing director or whole-time director under this Act, or any other law for the time being in force.

**Target s204** (Secretarial audit for bigger companies.)

> (1) Every listed company and a company belonging to other class of companies as may be prescribed shall annex with its Board’s report made in terms of sub-section (3) of section 134, a secretarial audit report, given by a company secretary in practice, in such form as may be prescribed. (2) It shall

```
question:
answer:
gold_clauses: ["s205(2)", "s204"]
anchor_clause: "s205(2)"
reference_path: [["s205(2)", "s204"]]
difficulty: one_hop
```

---

## 67. s2(70) -> s32

score 0.6025 | dissimilarity 0.8971 | target in-degree 1 | trigger `referred to in`

**Anchor s2(70)** (Definitions.)

> “prospectus” means any document described or issued as a prospectus and includes a red herring prospectus referred to in section 32 or shelf prospectus referred to in section 31 or any notice, circular, advertisement or other document inviting offers from the public for the subscription or purchase 

**Target s32** (Red herring prospectus.)

> (1) A company proposing to make an offer of securities may issue a red herring prospectus prior to the issue of a prospectus. (2) A company proposing to issue a red herring prospectus under sub-section (1) shall file it with the Registrar at least three days prior to the opening of the subscription 

```
question:
answer:
gold_clauses: ["s2(70)", "s32"]
anchor_clause: "s2(70)"
reference_path: [["s2(70)", "s32"]]
difficulty: one_hop
```

---

## 68. s388(1)(b) -> s40

score 0.6023 | dissimilarity 0.9468 | target in-degree 1 | trigger `none`

**Anchor s388(1)(b)** (Provisions as to expert’s consent and allotment.)

> if the prospectus does not have the effect, where an application is made in pursuance thereof, of rendering all persons concerned bound by all the provisions of sections 33 and 40, so far as applicable.

**Target s40** (Securities to be dealt with in stock exchanges.)

> (1) Every company making public offer shall, before making such offer, make an application to one or more recognised stock exchange or exchanges and obtain permission for the securities to be dealt with in such stock exchange or exchanges. (2) Where a prospectus states that an application under sub-

```
question:
answer:
gold_clauses: ["s388(1)(b)", "s40"]
anchor_clause: "s388(1)(b)"
reference_path: [["s388(1)(b)", "s40"]]
difficulty: one_hop
```

---

## 69. s174(3) -> s184(2)

score 0.602 | dissimilarity 0.9143 | target in-degree 2 | trigger `within the meaning of`

**Anchor s174(3)** (Quorum for meetings of Board.)

> Where at any time the number of interested directors exceeds or is equal to two-thirds of the total strength of the Board of Directors, the number of directors who are not interested directors and present at the meeting, being not less than two, shall be the quorum during such time. Explanation.— Fo

**Target s184(2)** (Disclosure of interest by director.)

> Every director of a company who is in any way, whether directly or indirectly, concerned or interested in a contract or arrangement or proposed contract or arrangement entered into or to be entered into— (a) with a body corporate in which such director or such director in association with any other 

```
question:
answer:
gold_clauses: ["s174(3)", "s184(2)"]
anchor_clause: "s174(3)"
reference_path: [["s174(3)", "s184(2)"]]
difficulty: one_hop
```

---

## 70. s321(1) -> s319

score 0.6014 | dissimilarity 0.8952 | target in-degree 1 | trigger `referred to in`

**Anchor s321(1)** (Arrangement when binding on company and creditors.)

> Any arrangement other than the arrangement referred to in section 319 entered into between the company which is about to be, or is in the course of being wound up and its creditors shall be binding on the company and on the creditors if it is sanctioned by a special resolution of the company and acc

**Target s319** (Power of Company Liquidator to accept shares, etc., as consideration for sale of property of company.)

> (1) Where a company (the transferor company) is proposed to be, or is in the course of being, wound up voluntarily and the whole or any part of its business or property is proposed to be transferred or sold to another company (the transferee company), the Company Liquidator of the transferor company

```
question:
answer:
gold_clauses: ["s321(1)", "s319"]
anchor_clause: "s321(1)"
reference_path: [["s321(1)", "s319"]]
difficulty: one_hop
```

---

## 71. s391(1) -> s35

score 0.6005 | dissimilarity 0.9438 | target in-degree 1 | trigger `none`

**Anchor s391(1)** (Application of sections 34 to 36 and Chapter XX.)

> The provisions of sections 34 to 36 (both inclusive) shall apply to— (i) the issue of a prospectus by a company incorporated outside India under section 389 as they apply to prospectus issued by an Indian company; (ii) the issue of Indian Depository Receipts by a foreign company.

**Target s35** (Civil liability for mis-statements in prospectus.)

> (1) Where a person has subscribed for securities of a company acting on any statement included, or the inclusion or omission of any matter, in the prospectus which is misleading and has sustained any loss or damage as a consequence thereof, the company and every person who— (a) is a director of the 

```
question:
answer:
gold_clauses: ["s391(1)", "s35"]
anchor_clause: "s391(1)"
reference_path: [["s391(1)", "s35"]]
difficulty: one_hop
```

---

## 72. s134(3)(e) -> s178(1)

score 0.5989 | dissimilarity 0.9091 | target in-degree 2 | trigger `under`

**Anchor s134(3)(e)** (Financial statement, Board’s report, etc.)

> in case of a company covered under sub-section (1) of section 178, company’s policy on directors’ appointment and remuneration including criteria for determining qualifications, positive attributes, independence of a director and other matters provided under sub-section (3) of section 178;

**Target s178(1)** (Nomination and Remuneration Committee and Stakeholders Relationship Committee.)

> The Board of Directors of every listed company and such other class or classes of companies, as may be prescribed shall constitute the Nomination and Remuneration Committee consisting of three or more non-executive directors out of which not less than one-half shall be independent directors: Provide

```
question:
answer:
gold_clauses: ["s134(3)(e)", "s178(1)"]
anchor_clause: "s134(3)(e)"
reference_path: [["s134(3)(e)", "s178(1)"]]
difficulty: one_hop
```

---

## 73. s107(1) -> s109

score 0.5963 | dissimilarity 0.9048 | target in-degree 2 | trigger `under`

**Anchor s107(1)** (Voting by show of hands.)

> At any general meeting, a resolution put to the vote of the meeting shall, unless a poll is demanded under section 109 or the voting is carried out electronically, be decided on a show of hands.

**Target s109** (Demand for poll.)

> (1) Before or on the declaration of the result of the voting on any resolution on show of hands, a poll may be ordered to be taken by the Chairman of the meeting on his own motion, and shall be ordered to be taken by him on a demand made in that behalf,— (a) in the case a company having a share capi

```
question:
answer:
gold_clauses: ["s107(1)", "s109"]
anchor_clause: "s107(1)"
reference_path: [["s107(1)", "s109"]]
difficulty: one_hop
```

---

## 74. s272(4) -> s271(1)

score 0.5945 | dissimilarity 0.8962 | target in-degree 1 | trigger `specified in`

**Anchor s272(4)** (Petition for winding up.)

> The Registrar shall be entitled to present a petition for winding up under subsection (1) on any of the grounds specified in sub-section (1) of section 271, except on the grounds specified in clause (b), clause (d) or clause (g) of that sub-section: Provided that the Registrar shall not present a pe

**Target s271(1)** (Circumstances in which company may be wound up by Tribunal.)

> A company may, on a petition under section 272, be wound up by the Tribunal,— (a) if the company is unable to pay its debts; (b) if the company has, by special resolution, resolved that the company be wound up by the Tribunal; (c) if the company has acted against the interests of the sovereignty and

```
question:
answer:
gold_clauses: ["s272(4)", "s271(1)"]
anchor_clause: "s272(4)"
reference_path: [["s272(4)", "s271(1)"]]
difficulty: one_hop
```

---

## 75. s399(1)(ii) -> s388(1)(b)

score 0.5942 | dissimilarity 0.9333 | target in-degree 1 | trigger `in pursuance of`

**Anchor s399(1)(ii)** (Inspection, production and evidence of documents kept by Registrar.)

> in relation to documents so delivered in pursuance of clause (b) of subsection (1) of section 388, only during the fourteen days beginning with the date of the prospectus; and at other times, only with the permission of the Central Government.

**Target s388(1)(b)** (Provisions as to expert’s consent and allotment.)

> if the prospectus does not have the effect, where an application is made in pursuance thereof, of rendering all persons concerned bound by all the provisions of sections 33 and 40, so far as applicable.

```
question:
answer:
gold_clauses: ["s399(1)(ii)", "s388(1)(b)"]
anchor_clause: "s399(1)(ii)"
reference_path: [["s399(1)(ii)", "s388(1)(b)"]]
difficulty: one_hop
```

---

## 76. s87(1)(c) -> s82

score 0.5931 | dissimilarity 0.9315 | target in-degree 1 | trigger `in pursuance of`

**Anchor s87(1)(c)** (Rectification by Central Government in register of charges.)

> the omission or mis-statement of any particular with respect to any such charge or modification or with respect to any memorandum of satisfaction or other entry made in pursuance of section 82 or section 83,

**Target s82** (Company to report satisfaction of charge.)

> (1) A company shall give intimation to the Registrar in the prescribed form, of the payment or satisfaction in full of any charge registered under this Chapter within a period of thirty days from the date of such payment or satisfaction and the provisions of sub-section (1) of section 77 shall, as f

```
question:
answer:
gold_clauses: ["s87(1)(c)", "s82"]
anchor_clause: "s87(1)(c)"
reference_path: [["s87(1)(c)", "s82"]]
difficulty: one_hop
```

---

## 77. s230(12) -> s66

score 0.5929 | dissimilarity 0.9312 | target in-degree 1 | trigger `none`

**Anchor s230(12)** (Power to compromise or make arrangements with creditors and members.)

> An aggrieved party may make an application to the Tribunal in the event of any grievances with respect to the takeover offer of companies other than listed companies in such manner as may be prescribed and the Tribunal may, on application, pass such order as it may deem fit. Explanation.— For the re

**Target s66** (Reduction of share capital.)

> (1) Subject to confirmation by the Tribunal on an application by the company, a company limited by shares or limited by guarantee and having a share capital may, by a special resolution, reduce the share capital in any manner and in particular, may— (a) extinguish or reduce the liability on any of i

```
question:
answer:
gold_clauses: ["s230(12)", "s66"]
anchor_clause: "s230(12)"
reference_path: [["s230(12)", "s66"]]
difficulty: one_hop
```

---

## 78. s388(1)(b) -> s33

score 0.5929 | dissimilarity 0.931 | target in-degree 1 | trigger `none`

**Anchor s388(1)(b)** (Provisions as to expert’s consent and allotment.)

> if the prospectus does not have the effect, where an application is made in pursuance thereof, of rendering all persons concerned bound by all the provisions of sections 33 and 40, so far as applicable.

**Target s33** (Issue of application forms for securities.)

> (1) No form of application for the purchase of any of the securities of a company shall be issued unless such form is accompanied by an abridged prospectus: Provided that nothing in this sub-section shall apply if it is shown that the form of application was issued — (a) in connection with a bona fi

```
question:
answer:
gold_clauses: ["s388(1)(b)", "s33"]
anchor_clause: "s388(1)(b)"
reference_path: [["s388(1)(b)", "s33"]]
difficulty: one_hop
```

---

## 79. s4(1) -> s8

score 0.591 | dissimilarity 0.8638 | target in-degree 3 | trigger `under`

**Anchor s4(1)** (Memorandum.)

> The memorandum of a company shall state— (a) the name of the company with the last word “Limited” in the case of a public limited company, or the last words “Private Limited” in the case of a private limited company: Provided that nothing in this clause shall apply to a company registered under sect

**Target s8** (Formulation of companies with charitable objects, etc.)

> (1) Where it is proved to the satisfaction of the Central Government that a person or an association of persons proposed to be registered under this Act as a limited company— (a) has in its objects the promotion of commerce, art, science, sports, education, research, social welfare, religion, charit

```
question:
answer:
gold_clauses: ["s4(1)", "s8"]
anchor_clause: "s4(1)"
reference_path: [["s4(1)", "s8"]]
difficulty: one_hop
```

---

## 80. s306(2)(a) -> s305

score 0.5907 | dissimilarity 0.9274 | target in-degree 1 | trigger `under`

**Anchor s306(2)(a)** (Meeting of creditors.)

> cause to be presented a full statement of the position of the affairs of the company together with a list of creditors of the company, if any, copy of declaration under section 305 and the estimated amount of the claims before such meeting; and

**Target s305** (Declaration of solvency in case of proposal to wind up voluntarily.)

> (1) Where it is proposed to wind up a company voluntarily, its director or directors, or in case the company has more than two directors, the majority of its directors, shall, at a meeting of the Board, make a declaration verified by an affidavit to the effect that they have made a full inquiry into

```
question:
answer:
gold_clauses: ["s306(2)(a)", "s305"]
anchor_clause: "s306(2)(a)"
reference_path: [["s306(2)(a)", "s305"]]
difficulty: one_hop
```

---

## 81. s117(3) -> s399

score 0.5904 | dissimilarity 0.927 | target in-degree 1 | trigger `under`

**Anchor s117(3)** (Resolutions and agreements to be filed.)

> The provisions of this section shall apply to— (a) special resolutions; (b) resolutions which have been agreed to by all the members of a company, but which, if not so agreed to, would not have been effective for their purpose unless they had been passed as special resolutions; (c) any resolution of

**Target s399** (Inspection, production and evidence of documents kept by Registrar.)

> (1) Save as otherwise provided elsewhere in this Act, any person may— (a) inspect by electronic means any documents kept by the Registrar in accordance with the rules made, being documents filed or registered by him in pursuance of this Act, or making a record of any fact required or authorised to b

```
question:
answer:
gold_clauses: ["s117(3)", "s399"]
anchor_clause: "s117(3)"
reference_path: [["s117(3)", "s399"]]
difficulty: one_hop
```

---

## 82. s458(1) -> s194

score 0.5898 | dissimilarity 0.9259 | target in-degree 1 | trigger `none`

**Anchor s458(1)** (Delegation by Central Government of its powers and functions.)

> The Central Government may, by notification, and subject to such conditions, limitations and restrictions as may be specified therein, delegate any of its powers or functions under this Act other than the power to make rules to such authority or officer as may be specified in the notification: Provi

**Target s194** (Prohibition on forward dealings in securities of company by director or key managerial personnel.)

> (1) No director of a company or any of its key managerial personnel shall buy in the company, or in its holding, subsidiary or associate company— (a) a right to call for delivery or a right to make delivery at a specified price and within a specified time, of a specified number of relevant shares or

```
question:
answer:
gold_clauses: ["s458(1)", "s194"]
anchor_clause: "s458(1)"
reference_path: [["s458(1)", "s194"]]
difficulty: one_hop
```

---

## 83. s310(2) -> s306(3)

score 0.5896 | dissimilarity 0.8936 | target in-degree 2 | trigger `under`

**Anchor s310(2)** (Appointment of Company Liquidator.)

> Where the creditors have passed a resolution for winding up the company under sub-section (3) of section 306, the appointment of the Company Liquidator under this section shall be effective only after it is approved by the majority of creditors in value of the company: Provided that where such credi

**Target s306(3)** (Meeting of creditors.)

> Where two-thirds in value of creditors of the company are of the opinion that— (a) it is in the interest of all parties that the company be wound up voluntarily, the company shall be wound up voluntarily; or (b) the company may not be able to pay for its debts in full from the proceeds of assets sol

```
question:
answer:
gold_clauses: ["s310(2)", "s306(3)"]
anchor_clause: "s310(2)"
reference_path: [["s310(2)", "s306(3)"]]
difficulty: one_hop
```

---

## 84. s384(3) -> s128

score 0.5892 | dissimilarity 0.925 | target in-degree 1 | trigger `none`

**Anchor s384(3)** (Debentures, annual return, registration of charges, books of account and their inspection.)

> The provisions of section 128 shall apply to a foreign company to the extent of requiring it to keep at its principal place of business in India, the books of account referred to in that section, with respect to monies received and spent, sales and purchases made, and assets and liabilities, in the 

**Target s128** (Books of account, etc., to be kept by company.)

> (1) Every company shall prepare and keep at its registered office books of account and other relevant books and papers and financial statement for every financial year which give a true and fair view of the state of the affairs of the company, including that of its branch office or offices, if any, 

```
question:
answer:
gold_clauses: ["s384(3)", "s128"]
anchor_clause: "s384(3)"
reference_path: [["s384(3)", "s128"]]
difficulty: one_hop
```

---

## 85. s147(1) -> s140

score 0.5886 | dissimilarity 0.9239 | target in-degree 1 | trigger `none`

**Anchor s147(1)** (Punishment for contravention.)

> If any of the provisions of sections 139 to 146 (both inclusive) is contravened, the company shall be punishable with fine which shall not be less than twenty-five thousand rupees but which may extend to five lakh rupees and every officer of the company who is in default shall be punishable with imp

**Target s140** (Removal, resignation of auditor and giving of special notice.)

> (1) The auditor appointed under section 139 may be removed from his office before the expiry of his term only by a special resolution of the company, after obtaining the previous approval of the Central Government in that behalf in the prescribed manner: Provided that before taking any action under 

```
question:
answer:
gold_clauses: ["s147(1)", "s140"]
anchor_clause: "s147(1)"
reference_path: [["s147(1)", "s140"]]
difficulty: one_hop
```

---

## 86. s171(1) -> s170(1)

score 0.5881 | dissimilarity 0.9231 | target in-degree 1 | trigger `under`

**Anchor s171(1)** (Members’ right to inspect.)

> The register kept under sub-section (1) of section 170,— (a) shall be open for inspection during business hours and the members shall have a right to take extracts therefrom and copies thereof, on a request by the members, be provided to them free of cost within thirty days; and (b) shall also be ke

**Target s170(1)** (Register of directors and key managerial personnel and their shareholding.)

> Every company shall keep at its registered office a register containing such particulars of its directors and key managerial personnel as may be prescribed, which shall include the details of securities held by each of them in the company or its holding, subsidiary, subsidiary of company’s holding c

```
question:
answer:
gold_clauses: ["s171(1)", "s170(1)"]
anchor_clause: "s171(1)"
reference_path: [["s171(1)", "s170(1)"]]
difficulty: one_hop
```

---

## 87. s13(1) -> s61

score 0.5875 | dissimilarity 0.9221 | target in-degree 1 | trigger `provided in`

**Anchor s13(1)** (Alteration of memorandum.)

> Save as provided in section 61, a company may, by a special resolution and after complying with the procedure specified in this section, alter the provisions of its memorandum.

**Target s61** (Power of limited company to alter its share capital.)

> (1) A limited company having a share capital may, if so authorised by its articles, alter its memorandum in its general meeting to— (a) increase its authorised share capital by such amount as it thinks expedient; (b) consolidate and divide all or any of its share capital into shares of a larger amou

```
question:
answer:
gold_clauses: ["s13(1)", "s61"]
anchor_clause: "s13(1)"
reference_path: [["s13(1)", "s61"]]
difficulty: one_hop
```

---

## 88. s232(1) -> s230(4)

score 0.587 | dissimilarity 0.9213 | target in-degree 1 | trigger `none`

**Anchor s232(1)** (Merger and amalgamation of companies.)

> Where an application is made to the Tribunal under section 230 for the sanctioning of a compromise or an arrangement proposed between a company and any such persons as are mentioned in that section, and it is shown to the Tribunal— (a) that the compromise or arrangement has been proposed for the pur

**Target s230(4)** (Power to compromise or make arrangements with creditors and members.)

> A notice under sub-section (3) shall provide that the persons to whom the notice is sent may vote in the meeting either themselves or through proxies or by postal ballot to the adoption of the compromise or arrangement within one month from the date of receipt of such notice: Provided that any objec

```
question:
answer:
gold_clauses: ["s232(1)", "s230(4)"]
anchor_clause: "s232(1)"
reference_path: [["s232(1)", "s230(4)"]]
difficulty: one_hop
```

---

## 89. s143(7) -> s139(5)

score 0.5856 | dissimilarity 0.8548 | target in-degree 3 | trigger `under`

**Anchor s143(7)** (Powers and duties of auditors and auditing standards.)

> Without prejudice to the provisions of this Chapter, the Comptroller and Auditor-General of India may, in case of any company covered under sub-section (5) or sub-section (7) of section 139, if he considers necessary, by an order, cause test audit to be conducted of the accounts of such company and 

**Target s139(5)** (Appointment of auditors.)

> Notwithstanding anything contained in sub-section (1), in the case of a Government company or any other company owned or controlled, directly or indirectly, by the Central Government, or by any State Government or Governments, or partly by the Central Government and partly by one or more State Gover

```
question:
answer:
gold_clauses: ["s143(7)", "s139(5)"]
anchor_clause: "s143(7)"
reference_path: [["s143(7)", "s139(5)"]]
difficulty: one_hop
```

---

## 90. s282(3) -> s340

score 0.5847 | dissimilarity 0.9175 | target in-degree 1 | trigger `under`

**Anchor s282(3)** (Directions of Tribunal on report of Company Liquidator.)

> Where a report is received from the Company Liquidator or the Central Government or any person that a fraud has been committed in respect of the company, the Tribunal shall, without prejudice to the process of winding up, order for investigation under section 210, and on consideration of the report 

**Target s340** (Power of Tribunal to assess damages against delinquent directors, etc.)

> (1) If in the course of winding up of a company, it appears that any person who has taken part in the promotion or formation of the company, or any person, who is or has been a director, manager, Company Liquidator or officer of the company— (a) has misapplied, or retained, or become liable or accou

```
question:
answer:
gold_clauses: ["s282(3)", "s340"]
anchor_clause: "s282(3)"
reference_path: [["s282(3)", "s340"]]
difficulty: one_hop
```

---

## 91. s458(1) -> s195

score 0.5846 | dissimilarity 0.9174 | target in-degree 1 | trigger `none`

**Anchor s458(1)** (Delegation by Central Government of its powers and functions.)

> The Central Government may, by notification, and subject to such conditions, limitations and restrictions as may be specified therein, delegate any of its powers or functions under this Act other than the power to make rules to such authority or officer as may be specified in the notification: Provi

**Target s195** (Prohibition on insider trading of securities.)

> (1) No person including any director or key managerial personnel of a company shall enter into insider trading: Provided that nothing contained in this sub-section shall apply to any communication required in the ordinary course of business or profession or employment or under any law. Explanation.—

```
question:
answer:
gold_clauses: ["s458(1)", "s195"]
anchor_clause: "s458(1)"
reference_path: [["s458(1)", "s195"]]
difficulty: one_hop
```

---

## 92. s271(1) -> s272

score 0.5836 | dissimilarity 0.8836 | target in-degree 2 | trigger `under`

**Anchor s271(1)** (Circumstances in which company may be wound up by Tribunal.)

> A company may, on a petition under section 272, be wound up by the Tribunal,— (a) if the company is unable to pay its debts; (b) if the company has, by special resolution, resolved that the company be wound up by the Tribunal; (c) if the company has acted against the interests of the sovereignty and

**Target s272** (Petition for winding up.)

> (1) Subject to the provisions of this section, a petition to the Tribunal for the winding up of a company shall be presented by— (a) the company; (b) any creditor or creditors, including any contingent or prospective creditor or creditors; (c) any contributory or contributories; (d) all or any of th

```
question:
answer:
gold_clauses: ["s271(1)", "s272"]
anchor_clause: "s271(1)"
reference_path: [["s271(1)", "s272"]]
difficulty: one_hop
```

---

## 93. s122(3) -> s114

score 0.5827 | dissimilarity 0.8571 | target in-degree 2 | trigger `for the purposes of`

**Anchor s122(3)** (Applicability of this Chapter to One Person Company.)

> For the purposes of section 114, any business which is required to be transacted at an annual general meeting or other general meeting of a company by means of an ordinary or special resolution, it shall be sufficient if, in case of One Person Company, the resolution is communicated by the member to

**Target s114** (Ordinary and special resolutions.)

> (1) A resolution shall be an ordinary resolution if the notice required under this Act has been duly given and it is required to be passed by the votes cast, whether on a show of hands, or electronically or on a poll, as the case may be, in favour of the resolution, including the casting vote, if an

```
question:
answer:
gold_clauses: ["s122(3)", "s114"]
anchor_clause: "s122(3)"
reference_path: [["s122(3)", "s114"]]
difficulty: one_hop
```

---

## 94. s143(7) -> s139(7)

score 0.5807 | dissimilarity 0.8788 | target in-degree 2 | trigger `under`

**Anchor s143(7)** (Powers and duties of auditors and auditing standards.)

> Without prejudice to the provisions of this Chapter, the Comptroller and Auditor-General of India may, in case of any company covered under sub-section (5) or sub-section (7) of section 139, if he considers necessary, by an order, cause test audit to be conducted of the accounts of such company and 

**Target s139(7)** (Appointment of auditors.)

> Notwithstanding anything contained in sub-section (1) or sub-section (5), in the case of a Government company or any other company owned or controlled, directly or indirectly, by the Central Government, or by any State Government, or Governments, or partly by the Central Government and partly by one

```
question:
answer:
gold_clauses: ["s143(7)", "s139(7)"]
anchor_clause: "s143(7)"
reference_path: [["s143(7)", "s139(7)"]]
difficulty: one_hop
```

---

## 95. s256(1)(b) -> s257

score 0.5804 | dissimilarity 0.9103 | target in-degree 1 | trigger `none`

**Anchor s256(1)(b)** (Appointment of interim administrator.)

> appoint an interim administrator to convene a meeting of creditors of the company in accordance with the provisions of section 257 to be held not later than forty-five days from receipt of the order of the Tribunal appointing him to consider whether on the basis of the particulars and documents furn

**Target s257** (Committee of creditors.)

> (1) The interim administrator shall appoint a committee of creditors with such number of members as he may determine, but not exceeding seven, and as far as possible a representative each of every class of creditors should be represented in that committee. (2) The holding of the meeting of the commi

```
question:
answer:
gold_clauses: ["s256(1)(b)", "s257"]
anchor_clause: "s256(1)(b)"
reference_path: [["s256(1)(b)", "s257"]]
difficulty: one_hop
```

---

## 96. s97(1) -> s96

score 0.5797 | dissimilarity 0.9091 | target in-degree 1 | trigger `under`

**Anchor s97(1)** (Power of Tribunal to call annual general meeting.)

> If any default is made in holding the annual general meeting of a company under section 96, the Tribunal may, notwithstanding anything contained in this Act or the articles of the company, on the application of any member of the company, call, or direct the calling of, an annual general meeting of t

**Target s96** (Annual general meeting.)

> (1) Every company other than a One Person Company shall in each year hold in addition to any other meetings, a general meeting as its annual general meeting and shall specify the meeting as such in the notices calling it, and not more than fifteen months shall elapse between the date of one annual g

```
question:
answer:
gold_clauses: ["s97(1)", "s96"]
anchor_clause: "s97(1)"
reference_path: [["s97(1)", "s96"]]
difficulty: one_hop
```

---

## 97. s224(2) -> s223

score 0.5795 | dissimilarity 0.8767 | target in-degree 2 | trigger `under`

**Anchor s224(2)** (Actions to be taken in pursuance of inspector’s report.)

> If any company or other body corporate is liable to be wound up under this Act and it appears to the Central Government from any such report made under section 223 that it is expedient so to do by reason of any such circumstances as are referred to in section 213, the Central Government may, unless 

**Target s223** (Inspector’s report.)

> (1) An inspector appointed under this Chapter may, and if so directed by the Central Government shall, submit interim reports to that Government, and on the conclusion of the investigation, shall submit a final report to the Central Government. (2) Every report made under sub-section (1) shall be in

```
question:
answer:
gold_clauses: ["s224(2)", "s223"]
anchor_clause: "s224(2)"
reference_path: [["s224(2)", "s223"]]
difficulty: one_hop
```

---

## 98. s231(2) -> s273

score 0.5791 | dissimilarity 0.908 | target in-degree 1 | trigger `under`

**Anchor s231(2)** (Power of Tribunal to enforce compromise or arrangement.)

> If the Tribunal is satisfied that the compromise or arrangement sanctioned under section 230 cannot be implemented satisfactorily with or without modifications, and the company is unable to pay its debts as per the scheme, it may make an order for winding up the company and such an order shall be de

**Target s273** (Powers of Tribunal.)

> (1) The Tribunal may, on receipt of a petition for winding up under section 272 pass any of the following orders, namely:— (a) dismiss it, with or without costs; (b) make any interim order as it thinks fit; (c) appoint a provisional liquidator of the company till the making of a winding up order; (d

```
question:
answer:
gold_clauses: ["s231(2)", "s273"]
anchor_clause: "s231(2)"
reference_path: [["s231(2)", "s273"]]
difficulty: one_hop
```

---

## 99. s87(1)(c) -> s83

score 0.5785 | dissimilarity 0.875 | target in-degree 2 | trigger `none`

**Anchor s87(1)(c)** (Rectification by Central Government in register of charges.)

> the omission or mis-statement of any particular with respect to any such charge or modification or with respect to any memorandum of satisfaction or other entry made in pursuance of section 82 or section 83,

**Target s83** (Power of Registrar to make entries of satisfaction and release in absence of intimation from company.)

> (1) The Registrar may, on evidence being given to his satisfaction with respect to any registered charge,— (a) that the debt for which the charge was given has been paid or satisfied in whole or in part; or (b) that part of the property or undertaking charged has been released from the charge or has

```
question:
answer:
gold_clauses: ["s87(1)(c)", "s83"]
anchor_clause: "s87(1)(c)"
reference_path: [["s87(1)(c)", "s83"]]
difficulty: one_hop
```

---

## 100. s217(1) -> s219

score 0.5785 | dissimilarity 0.875 | target in-degree 2 | trigger `under`

**Anchor s217(1)** (Procedure, powers, etc., of inspectors.)

> It shall be the duty of all officers and other employees and agents including the former officers, employees and agents of a company which is under investigation in accordance with the provisions contained in this Chapter, and where the affairs of any other body corporate or a person are investigate

**Target s219** (Power of inspector to conduct investigation into affairs of related companies, etc.)

> If an inspector appointed under section 210 or section 212 or section 213 to investigate into the affairs of a company considers it necessary for the purposes of the investigation, to investigate also the affairs of— (a) any other body corporate which is, or has at any relevant time been the company

```
question:
answer:
gold_clauses: ["s217(1)", "s219"]
anchor_clause: "s217(1)"
reference_path: [["s217(1)", "s219"]]
difficulty: one_hop
```

---

## 101. s42(2) -> s62(1)(b)

score 0.5784 | dissimilarity 0.907 | target in-degree 1 | trigger `none`

**Anchor s42(2)** (Offer or invitation for subscription of securities on private placement.)

> Subject to sub-section (1), the offer of securities or invitation to subscribe securities, shall be made to such number of persons not exceeding fifty or such higher number as may be prescribed, excluding qualified institutional buyers and employees of the company being offered securities under a sc

**Target s62(1)(b)** (Further issue of share capital.)

> to employees under a scheme of employees’ stock option, subject to special resolution passed by company and subject to such conditions as may be prescribed; or

```
question:
answer:
gold_clauses: ["s42(2)", "s62(1)(b)"]
anchor_clause: "s42(2)"
reference_path: [["s42(2)", "s62(1)(b)"]]
difficulty: one_hop
```

---

## 102. s262(1) -> s261

score 0.5778 | dissimilarity 0.9059 | target in-degree 1 | trigger `under`

**Anchor s262(1)** (Sanction of scheme.)

> The scheme prepared by the company administrator under section 261 shall be placed before the creditors of the sick company in a meeting convened for their approval by the company administrator within the period of sixty days from his appointment, which may be extended by the Tribunal up to a period

**Target s261** (Scheme of revival and rehabilitation.)

> (1) The company administrator shall prepare or cause to be prepared a scheme of revival and rehabilitation of the sick company after considering the draft scheme filed along with the application under section 254. (2) A scheme prepared in relation to any sick company under sub-section (1) may provid

```
question:
answer:
gold_clauses: ["s262(1)", "s261"]
anchor_clause: "s262(1)"
reference_path: [["s262(1)", "s261"]]
difficulty: one_hop
```

---

## 103. s94(1) -> s88

score 0.5776 | dissimilarity 0.9057 | target in-degree 1 | trigger `under`

**Anchor s94(1)** (Place of keeping and inspection of registers, returns, etc.)

> The registers required to be kept and maintained by a company under section 88 and copies of the annual return filed under section 92 shall be kept at the registered office of the company: Provided that such registers or copies of return may also be kept at any other place in India in which more tha

**Target s88** (Register of members, etc.)

> (1) Every company shall keep and maintain the following registers in such form and in such manner as may be prescribed, namely:— (a) register of members indicating separately for each class of equity and preference shares held by each member residing in or outside India; (b) register of debenture-ho

```
question:
answer:
gold_clauses: ["s94(1)", "s88"]
anchor_clause: "s94(1)"
reference_path: [["s94(1)", "s88"]]
difficulty: one_hop
```

---

## 104. s225(1) -> s214

score 0.5764 | dissimilarity 0.9036 | target in-degree 1 | trigger `under`

**Anchor s225(1)** (Expenses of investigation.)

> The expenses of, and incidental to, an investigation by an inspector appointed by the Central Government under this Chapter other than expenses of inspection under section 214 shall be defrayed in the first instance by the Central Government, but shall be reimbursed by the following persons to the e

**Target s214** (Security for payment of costs and expenses of investigation.)

> Where an investigation is ordered by the Central Government in pursuance of clause (b) of sub-section (1) of section 210, or in pursuance of an order made by the Tribunal under section 213, the Central Government may before appointing an inspector under subsection (3) of section 210 or clause (b) of

```
question:
answer:
gold_clauses: ["s225(1)", "s214"]
anchor_clause: "s225(1)"
reference_path: [["s225(1)", "s214"]]
difficulty: one_hop
```

---

## 105. s66(8) -> s271(2)

score 0.5753 | dissimilarity 0.9018 | target in-degree 1 | trigger `within the meaning of`

**Anchor s66(8)** (Reduction of share capital.)

> Where the name of any creditor entitled to object to the reduction of share capital under this section is, by reason of his ignorance of the proceedings for reduction or of their nature and effect with respect to his debt or claim, not entered on the list of creditors, and after such reduction, the 

**Target s271(2)** (Circumstances in which company may be wound up by Tribunal.)

> A company shall be deemed to be unable to pay its debts,— (a) if a creditor, by assignment or otherwise, to whom the company is indebted for an amount exceeding one lakh rupees then due, has served on the company, by causing it to be delivered at its registered office, by registered post or otherwis

```
question:
answer:
gold_clauses: ["s66(8)", "s271(2)"]
anchor_clause: "s66(8)"
reference_path: [["s66(8)", "s271(2)"]]
difficulty: one_hop
```

---

## 106. s8(9) -> s269

score 0.5751 | dissimilarity 0.9014 | target in-degree 1 | trigger `under`

**Anchor s8(9)** (Formulation of companies with charitable objects, etc.)

> If on the winding up or dissolution of a company registered under this section, there remains, after the satisfaction of its debts and liabilities, any asset, they may be transferred to another company registered under this section and having similar objects, subject to such conditions as the Tribun

**Target s269** (Rehabilitation and insolvency fund.)

> (1) There shall be formed a Fund to be called the Rehabilitation and Insolvency Fund for the purposes of rehabilitation, revival and liquidation of the sick companies. (2) There shall be credited to the Fund— (a) the grants made by the Central Government for the purposes of the Fund; (b) the amount 

```
question:
answer:
gold_clauses: ["s8(9)", "s269"]
anchor_clause: "s8(9)"
reference_path: [["s8(9)", "s269"]]
difficulty: one_hop
```

---

## 107. s173(5) -> s174

score 0.5724 | dissimilarity 0.8969 | target in-degree 1 | trigger `none`

**Anchor s173(5)** (Meetings of Board.)

> A One Person Company, small company and dormant company shall be deemed to have complied with the provisions of this section if at least one meeting of the Board of Directors has been conducted in each half of a calendar year and the gap between the two meetings is not less than ninety days: Provide

**Target s174** (Quorum for meetings of Board.)

> (1) The quorum for a meeting of the Board of Directors of a company shall be one-third of its total strength or two directors, whichever is higher, and the participation of the directors by video conferencing or by other audio visual means shall also be counted for the purposes of quorum under this 

```
question:
answer:
gold_clauses: ["s173(5)", "s174"]
anchor_clause: "s173(5)"
reference_path: [["s173(5)", "s174"]]
difficulty: one_hop
```

---

## 108. s282(3) -> s339

score 0.572 | dissimilarity 0.8963 | target in-degree 1 | trigger `under`

**Anchor s282(3)** (Directions of Tribunal on report of Company Liquidator.)

> Where a report is received from the Company Liquidator or the Central Government or any person that a fraud has been committed in respect of the company, the Tribunal shall, without prejudice to the process of winding up, order for investigation under section 210, and on consideration of the report 

**Target s339** (Liability for fraudulent conduct of business.)

> (1) If in the course of the winding up of a company, it appears that any business of the company has been carried on with intent to defraud creditors of the company or any other persons or for any fraudulent purpose, the Tribunal, on the application of the Official Liquidator, or the Company Liquida

```
question:
answer:
gold_clauses: ["s282(3)", "s339"]
anchor_clause: "s282(3)"
reference_path: [["s282(3)", "s339"]]
difficulty: one_hop
```

---

## 109. s391(1) -> s34

score 0.5717 | dissimilarity 0.8958 | target in-degree 1 | trigger `none`

**Anchor s391(1)** (Application of sections 34 to 36 and Chapter XX.)

> The provisions of sections 34 to 36 (both inclusive) shall apply to— (i) the issue of a prospectus by a company incorporated outside India under section 389 as they apply to prospectus issued by an Indian company; (ii) the issue of Indian Depository Receipts by a foreign company.

**Target s34** (Criminal liability for mis-statements in prospectus.)

> Where a prospectus, issued, circulated or distributed under this Chapter, includes any statement which is untrue or misleading in form or context in which it is included or where any inclusion or omission of any matter is likely to mislead, every person who authorises the issue of such prospectus sh

```
question:
answer:
gold_clauses: ["s391(1)", "s34"]
anchor_clause: "s391(1)"
reference_path: [["s391(1)", "s34"]]
difficulty: one_hop
```

---

## 110. s136(1) -> s101

score 0.5716 | dissimilarity 0.8636 | target in-degree 2 | trigger `none`

**Anchor s136(1)** (Right of member to copies of audited financial statement.)

> Without prejudice to the provisions of section 101, a copy of the financial statements, including consolidated financial statements, if any, auditor’s report and every other document required by law to be annexed or attached to the financial statements, which are to be laid before a company in its g

**Target s101** (Notice of meeting.)

> (1) A general meeting of a company may be called by giving not less than clear twenty-one days’ notice either in writing or through electronic mode in such manner as may be prescribed: Provided that a general meeting may be called after giving a shorter notice if consent is given in writing or by el

```
question:
answer:
gold_clauses: ["s136(1)", "s101"]
anchor_clause: "s136(1)"
reference_path: [["s136(1)", "s101"]]
difficulty: one_hop
```

---

## 111. s352(5) -> s348(1)

score 0.5711 | dissimilarity 0.8947 | target in-degree 1 | trigger `in pursuance of`

**Anchor s352(5)** (Company Liquidation Dividend and Undistributed Assets Account.)

> Where a company is being wound up voluntarily, the Company Liquidator shall, when filing a statement in pursuance of sub-section (1) of section 348, indicate the sum of money which is payable under sub-sections (1) and (2) of this section during the six months preceding the date on which the said st

**Target s348(1)** (Information as to pending liquidations.)

> If the winding up of a company is not concluded within one year after its commencement, the Company Liquidator shall, unless he is exempted from so doing either wholly or in part by the Central Government, within two months of the expiry of such year and thereafter until the winding up is concluded,

```
question:
answer:
gold_clauses: ["s352(5)", "s348(1)"]
anchor_clause: "s352(5)"
reference_path: [["s352(5)", "s348(1)"]]
difficulty: one_hop
```

---

## 112. s274(3) -> s273(1)(d)

score 0.5699 | dissimilarity 0.8929 | target in-degree 1 | trigger `under`

**Anchor s274(3)** (Direction for filing statement of affairs.)

> The directors and other officers of the company, in respect of which an order for winding up is passed by the Tribunal under clause (d) of sub-section (1) of section 273, shall, within a period of thirty days of such order, submit, at the cost of the company, the books of account of the company comp

**Target s273(1)(d)** (Powers of Tribunal.)

> make an order for the winding up of the company with or without costs; or

```
question:
answer:
gold_clauses: ["s274(3)", "s273(1)(d)"]
anchor_clause: "s274(3)"
reference_path: [["s274(3)", "s273(1)(d)"]]
difficulty: one_hop
```

---

## 113. s221(1) -> s244(1)

score 0.5689 | dissimilarity 0.8911 | target in-degree 1 | trigger `under`

**Anchor s221(1)** (Freezing of assets of company on inquiry and investigation.)

> Where it appears to the Tribunal, on a reference made to it by the Central Government or in connection with any inquiry or investigation into the affairs of a company under this Chapter or on any complaint made by such number of members as specified under sub-section (1) of section 244 or a creditor

**Target s244(1)** (Right to apply under section 241.)

> The following members of a company shall have the right to apply under section 241, namely:— (a) in the case of a company having a share capital, not less than one hundred members of the company or not less than one-tenth of the total number of its members, whichever is less, or any member or member

```
question:
answer:
gold_clauses: ["s221(1)", "s244(1)"]
anchor_clause: "s221(1)"
reference_path: [["s221(1)", "s244(1)"]]
difficulty: one_hop
```

---

## 114. s241(1) -> s244

score 0.5682 | dissimilarity 0.89 | target in-degree 1 | trigger `under`

**Anchor s241(1)** (Application to Tribunal for relief in cases of oppression, etc.)

> Any member of a company who complains that— (a) the affairs of the company have been or are being conducted in a manner prejudicial to public interest or in a manner prejudicial or oppressive to him or any other member or members or in a manner prejudicial to the interests of the company; or (b) the

**Target s244** (Right to apply under section 241.)

> (1) The following members of a company shall have the right to apply under section 241, namely:— (a) in the case of a company having a share capital, not less than one hundred members of the company or not less than one-tenth of the total number of its members, whichever is less, or any member or me

```
question:
answer:
gold_clauses: ["s241(1)", "s244"]
anchor_clause: "s241(1)"
reference_path: [["s241(1)", "s244"]]
difficulty: one_hop
```

---

## 115. s189(2) -> s184(1)

score 0.5678 | dissimilarity 0.8519 | target in-degree 1 | trigger `specified in`

**Anchor s189(2)** (Register of contracts or arrangements in which directors are interested.)

> Every director or key managerial personnel shall, within a period of thirty days of his appointment, or relinquishment of his office, as the case may be, disclose to the company the particulars specified in subsection (1) of section 184 relating to his concern or interest in the other associations w

**Target s184(1)** (Disclosure of interest by director.)

> Every director shall at the first meeting of the Board in which he participates as a director and thereafter at the first meeting of the Board in every financial year or whenever there is any change in the disclosures already made, then at the first Board meeting held after such change, disclose his

```
question:
answer:
gold_clauses: ["s189(2)", "s184(1)"]
anchor_clause: "s189(2)"
reference_path: [["s189(2)", "s184(1)"]]
difficulty: one_hop
```

---

## 116. s183(1) -> s182

score 0.5676 | dissimilarity 0.8889 | target in-degree 1 | trigger `none`

**Anchor s183(1)** (Power of Board and other persons to make contributions to national defence fund, etc.)

> The Board of Directors of any company or any person or authority exercising the powers of the Board of Directors of a company, or of the company in general meeting, may, notwithstanding anything contained in sections 180, 181 and section 182 or any other provision of this Act or in the memorandum, a

**Target s182** (Prohibitions and restrictions regarding political contributions.)

> (1) Notwithstanding anything contained in any other provision of this Act, a company, other than a Government company and a company which has been in existence for less than three financial years, may contribute any amount directly or indirectly to any political party: Provided that the amount refer

```
question:
answer:
gold_clauses: ["s183(1)", "s182"]
anchor_clause: "s183(1)"
reference_path: [["s183(1)", "s182"]]
difficulty: one_hop
```

---

## 117. s282(3) -> s342

score 0.5671 | dissimilarity 0.8881 | target in-degree 1 | trigger `under`

**Anchor s282(3)** (Directions of Tribunal on report of Company Liquidator.)

> Where a report is received from the Company Liquidator or the Central Government or any person that a fraud has been committed in respect of the company, the Tribunal shall, without prejudice to the process of winding up, order for investigation under section 210, and on consideration of the report 

**Target s342** (Prosecution of delinquent officers and members of company.)

> (1) If it appears to the Tribunal in the course of a winding up by the Tribunal, that any person, who is or has been an officer, or any member, of the company has been guilty of any offence in relation to the company, the Tribunal may, either on the application of any person interested in the windin

```
question:
answer:
gold_clauses: ["s282(3)", "s342"]
anchor_clause: "s282(3)"
reference_path: [["s282(3)", "s342"]]
difficulty: one_hop
```

---

## 118. s436(1)(a) -> s435(1)

score 0.565 | dissimilarity 0.8846 | target in-degree 1 | trigger `under`

**Anchor s436(1)(a)** (Offences triable by Special Courts.)

> all offences specified under sub-section (1) of section 435 shall be triable only by the Special Court established for the area in which the registered office of the company in relation to which the offence is committed or where there are more Special Courts than one for such area, by such one of th

**Target s435(1)** (Establishment of Special Courts.)

> The Central Government may, for the purpose of providing speedy trial of offences punishable under this Act with imprisonment of two years or more, by notification, establish or designate as many Special Courts as may be necessary: Provided that all other offences shall be tried, as the case may be,

```
question:
answer:
gold_clauses: ["s436(1)(a)", "s435(1)"]
anchor_clause: "s436(1)(a)"
reference_path: [["s436(1)(a)", "s435(1)"]]
difficulty: one_hop
```

---

## 119. s68(11) -> s70

score 0.5645 | dissimilarity 0.8837 | target in-degree 1 | trigger `none`

**Anchor s68(11)** (Power of company to purchase its own securities.)

> If a company makes any default in complying with the provisions of this section or any regulation made by the Securities and Exchange Board, for the purposes of clause (f) of sub-section (2), the company shall be punishable with fine which shall not be less than one lakh rupees but which may extend 

**Target s70** (Prohibition for buy-back in certain circumstances.)

> (1) No company shall directly or indirectly purchase its own shares or other specified securities— (a) through any subsidiary company including its own subsidiary companies; (b) through any investment company or group of investment companies; or (c) if a default, is made by the company, in the repay

```
question:
answer:
gold_clauses: ["s68(11)", "s70"]
anchor_clause: "s68(11)"
reference_path: [["s68(11)", "s70"]]
difficulty: one_hop
```

---

## 120. s233(12) -> s232(1)(b)

score 0.5636 | dissimilarity 0.8824 | target in-degree 1 | trigger `none`

**Anchor s233(12)** (Merger or amalgamation of certain companies.)

> The provisions of this section shall mutatis mutandis apply to a company or companies specified in sub-section (1) in respect of a scheme of compromise or arrangement referred to in section 230 or division or transfer of a company referred to clause (b) of subsection (1) of section 232.

**Target s232(1)(b)** (Merger and amalgamation of companies.)

> that under the scheme, the whole or any part of the undertaking, property or liabilities of any company (hereinafter referred to as the transferor company) is required to be transferred to another company (hereinafter referred to as the transferee company), or is proposed to be divided among and tra

```
question:
answer:
gold_clauses: ["s233(12)", "s232(1)(b)"]
anchor_clause: "s233(12)"
reference_path: [["s233(12)", "s232(1)(b)"]]
difficulty: one_hop
```

---
