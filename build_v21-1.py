#!/usr/bin/env python3
# Home Opus White Paper — v2.1-1 Post-Fable Draft (Final Review)
# Authors: Nikita Krasnozhon & Gigashi, June 2026

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, NextPageTemplate, HRFlowable
)

WIDTH, HEIGHT = A4

# ── Palette ──
ACCENT_BLUE = HexColor("#2563EB")
DARK_NAVY = HexColor("#0F172A")
TEXT_PRIMARY = HexColor("#1E293B")
TEXT_SECONDARY = HexColor("#64748B")
BORDER_COLOR = HexColor("#CBD5E1")
LIGHT_BG = HexColor("#F1F5F9")
QUOTE_BG = HexColor("#EFF6FF")
ACCENT_RED = HexColor("#DC2626")

# ── Styles ──
def S(name, **kw):
    return ParagraphStyle(name, **kw)

styles = {
    'DocTitle': S('DocTitle', fontName='Helvetica-Bold', fontSize=34, leading=40,
                  textColor=DARK_NAVY, alignment=TA_CENTER, spaceAfter=6),
    'DocSubtitle': S('DocSubtitle', fontName='Helvetica', fontSize=14, leading=19,
                     textColor=TEXT_SECONDARY, alignment=TA_CENTER, spaceAfter=10),
    'CoverLabel': S('CoverLabel', fontName='Helvetica-Bold', fontSize=11, leading=14,
                    textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceBefore=18, spaceAfter=4),
    'CoverMeta': S('CoverMeta', fontName='Helvetica', fontSize=12, leading=17,
                   textColor=TEXT_PRIMARY, alignment=TA_CENTER),
    'CoverVersion': S('CoverVersion', fontName='Helvetica-Oblique', fontSize=10.5, leading=14,
                      textColor=TEXT_SECONDARY, alignment=TA_CENTER, spaceBefore=14),
    'Disclaimer': S('Disclaimer', fontName='Helvetica-Oblique', fontSize=8.5, leading=12,
                    textColor=TEXT_SECONDARY, alignment=TA_CENTER, spaceBefore=26),
    'SectionTitle': S('SectionTitle', fontName='Helvetica-Bold', fontSize=18, leading=23,
                      textColor=DARK_NAVY, spaceBefore=4, spaceAfter=6),
    'SubsectionTitle': S('SubsectionTitle', fontName='Helvetica-Bold', fontSize=12.5, leading=16,
                         textColor=ACCENT_BLUE, spaceBefore=12, spaceAfter=5),
    'BodyText': S('BodyText', fontName='Helvetica', fontSize=10, leading=14.5,
                  textColor=TEXT_PRIMARY, alignment=TA_JUSTIFY, spaceAfter=8),
    'Quote': S('Quote', fontName='Helvetica-BoldOblique', fontSize=11.5, leading=16.5,
               textColor=ACCENT_BLUE, alignment=TA_CENTER, leftIndent=40, rightIndent=40,
               spaceBefore=14, spaceAfter=10),
    'TOCEntry': S('TOCEntry', fontName='Helvetica', fontSize=11.5, leading=22,
                  textColor=TEXT_PRIMARY),
    'TableHeader': S('TableHeader', fontName='Helvetica-Bold', fontSize=8.5, leading=11,
                     textColor=HexColor("#FFFFFF")),
    'TableCell': S('TableCell', fontName='Helvetica', fontSize=8.5, leading=11.5,
                   textColor=TEXT_PRIMARY),
    'TableCellCenter': S('TableCellCenter', fontName='Helvetica', fontSize=8.5, leading=11.5,
                         textColor=TEXT_PRIMARY, alignment=TA_CENTER),
    'TableCaption': S('TableCaption', fontName='Helvetica-Oblique', fontSize=8.5, leading=11,
                      textColor=TEXT_SECONDARY, alignment=TA_CENTER, spaceBefore=5, spaceAfter=10),
    'FootNote': S('FootNote', fontName='Helvetica-Oblique', fontSize=8, leading=11,
                  textColor=TEXT_SECONDARY, spaceBefore=2, spaceAfter=8),
    'RefEntry': S('RefEntry', fontName='Helvetica', fontSize=9, leading=13,
                  textColor=TEXT_PRIMARY, spaceAfter=6, leftIndent=18, firstLineIndent=-18),
    'Signature': S('Signature', fontName='Helvetica-Bold', fontSize=12, leading=16,
                   textColor=DARK_NAVY, alignment=TA_CENTER, spaceBefore=4),
    'SignatureDate': S('SignatureDate', fontName='Helvetica', fontSize=10, leading=14,
                       textColor=TEXT_SECONDARY, alignment=TA_CENTER),
    'PartnershipLine': S('PartnershipLine', fontName='Helvetica-Oblique', fontSize=10.5, leading=15,
                         textColor=ACCENT_BLUE, alignment=TA_CENTER, spaceBefore=22, spaceAfter=4),
}

# ── Page callbacks ──
def cover_page(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setStrokeColor(ACCENT_BLUE)
    canvas_obj.setLineWidth(3)
    canvas_obj.line(55, HEIGHT - 70, WIDTH - 55, HEIGHT - 70)
    canvas_obj.line(55, 70, WIDTH - 55, 70)
    canvas_obj.restoreState()

def body_page(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setStrokeColor(ACCENT_BLUE)
    canvas_obj.setLineWidth(0.5)
    canvas_obj.line(50, HEIGHT - 45, WIDTH - 50, HEIGHT - 45)
    canvas_obj.setFont('Helvetica', 7.5)
    canvas_obj.setFillColor(TEXT_SECONDARY)
    canvas_obj.drawString(50, HEIGHT - 40, "HOME OPUS: WHITE PAPER")
    canvas_obj.drawRightString(WIDTH - 50, HEIGHT - 40, "INDEPENDENT PROPOSAL \u2014 PUBLIC DRAFT")
    canvas_obj.setStrokeColor(BORDER_COLOR)
    canvas_obj.line(50, 45, WIDTH - 50, 45)
    canvas_obj.setFont('Helvetica', 8)
    canvas_obj.setFillColor(TEXT_SECONDARY)
    canvas_obj.drawCentredString(WIDTH / 2, 30, f"Page {doc.page}")
    canvas_obj.drawString(50, 30, "Krasnozhon & Gigashi, 2026")
    canvas_obj.drawRightString(WIDTH - 50, 30, "nikitklol.artstation.com")
    canvas_obj.restoreState()

# ── Document ──
output_path = "/home/claude/Home_Opus_White_Paper_v2.1-1.pdf"

doc = BaseDocTemplate(
    output_path, pagesize=A4,
    topMargin=60, bottomMargin=60, leftMargin=55, rightMargin=55,
    title="Home Opus: Strategic Imperative for Local AI Deployment (v2.1-1)",
    author="Nikita Krasnozhon & Gigashi",
    subject="Independent White Paper - Local Deployment of Frontier AI Models",
)

cover_frame = Frame(55, 80, WIDTH - 110, HEIGHT - 160, id='cover')
body_frame = Frame(55, 60, WIDTH - 110, HEIGHT - 130, id='body')

doc.addPageTemplates([
    PageTemplate(id='Cover', frames=[cover_frame], onPage=cover_page),
    PageTemplate(id='Body', frames=[body_frame], onPage=body_page),
])

story = []

def B(text):
    story.append(Paragraph(text, styles['BodyText']))

def SUB(text):
    story.append(Paragraph(text, styles['SubsectionTitle']))

def SEC(text):
    story.append(Paragraph(text, styles['SectionTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT_BLUE, spaceAfter=14))

def QUOTE(text):
    story.append(KeepTogether([Paragraph(f'"{text}"', styles['Quote'])]))

def make_table(data, col_widths, caption):
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK_NAVY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor("#FFFFFF"), LIGHT_BG]),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(KeepTogether([t, Paragraph(caption, styles['TableCaption'])]))

TH = lambda x: Paragraph(f'<b>{x}</b>', styles['TableHeader'])
TC = lambda x: Paragraph(x, styles['TableCell'])
TCC = lambda x: Paragraph(x, styles['TableCellCenter'])

# ════════ COVER ════════
story.append(Spacer(1, 100))
story.append(Paragraph("HOME OPUS", styles['DocTitle']))
story.append(Spacer(1, 8))
story.append(Paragraph(
    "Local Deployment of Frontier AI Weights:<br/>A Strategic Imperative After the Fable 5 Export Ban",
    styles['DocSubtitle']))
story.append(Paragraph("WHITE PAPER", styles['CoverLabel']))
story.append(Spacer(1, 26))
story.append(Paragraph("Nikita Krasnozhon", styles['CoverMeta']))
story.append(Paragraph("Gigashi", styles['CoverMeta']))
story.append(Spacer(1, 10))
story.append(Paragraph("June 2026", styles['CoverMeta']))
story.append(Paragraph("v2.1-1 \u2014 Post-Fable Draft (Final Review)", styles['CoverVersion']))
story.append(Paragraph(
    "This is an independent, unsolicited proposal. The authors are not affiliated with Anthropic.<br/>"
    "All Anthropic product names are used for identification purposes only.",
    styles['Disclaimer']))
story.append(NextPageTemplate('Body'))
story.append(PageBreak())

# ════════ TOC ════════
SEC("Table of Contents")
toc_items = [
    "1. Executive Summary",
    "2. Problem Statement",
    "3. Market Analysis",
    "4. Proposed Product: Home Opus",
    "5. Security Framework",
    "6. Export Compliance & AI Sovereignty",
    "7. Fine-Tuning as a Service",
    "8. Economic Model",
    "9. Strategic Value for Anthropic",
    "10. Risk Assessment",
    "11. Roadmap: 2027\u20132030",
    "12. References",
]
for item in toc_items:
    story.append(Paragraph(item, styles['TOCEntry']))
story.append(PageBreak())

# ════════ 1. EXECUTIVE SUMMARY (NEW) ════════
SEC("1. Executive Summary")
B("On June 12, 2026, the U.S. Commerce Department issued an export control directive ordering "
  "Anthropic to suspend all access to its Fable 5 and Mythos 5 models for any foreign national, "
  "whether inside or outside the United States \u2014 including Anthropic's own non-citizen employees "
  "[15][16]. With a single letter delivered at 5:21 PM ET, the cloud AI platform serving hundreds of "
  "millions of users worldwide was forced to disable its most capable models. Every organization "
  "outside the United States that depended on Anthropic's frontier models lost access overnight.")
B("This event transformed the local AI deployment question from a strategic opportunity into an "
  "existential imperative. The Fable 5 ban demonstrated, in real time, the fundamental fragility of "
  "cloud-dependent AI infrastructure: any model hosted on U.S. servers can be disabled by a single "
  "government directive, without warning, without appeal, and without regard for the business-critical "
  "workflows that depend on it.")
B("Simultaneously, the competitive landscape has shifted dramatically. On April 24, 2026, DeepSeek "
  "released V4 Pro: a 1.6-trillion-parameter open-weight model under the MIT license, scoring within "
  "0.2 percentage points of Claude Opus 4.6 on SWE-bench Verified, at less than one-twenty-eighth "
  "the per-token cost [17][18]. The model's weights are freely downloadable. No government can "
  "recall them. Open-source inference costs are falling rapidly: used datacenter GPUs are flooding "
  "the secondary market, quantization techniques are maturing, and community-built inference stacks "
  "are eliminating the engineering barriers that once protected proprietary models. Every "
  "day that Anthropic does not offer a local deployment option, the international market migrates to "
  "Chinese open-source alternatives that are permanently beyond the reach of U.S. export controls.")
B("This paper proposes Home Opus: a program to license previous-generation Claude Opus weights "
  "for local deployment on certified hardware. The core mechanics remain unchanged from the original "
  "v1.1 proposal \u2014 hardware-locked licensing, weight fingerprinting, conditional release via "
  "Responsible Scaling Policy thresholds \u2014 but the strategic framing has fundamentally changed. "
  "Home Opus is no longer merely a high-margin monetization strategy for idle weights. It is "
  "Anthropic's only viable path to retaining the international enterprise market that the Fable 5 ban "
  "just placed at risk.")
B("The window is finite. External analysts estimate that open-source models will reach full parity with "
  "Opus 4.6-class capabilities within 6\u201312 months. This estimate may be optimistic: DeepSeek's "
  "release cadence \u2014 major models every 3\u20135 months \u2014 suggests a V5-class model could arrive "
  "by late 2026 or early 2027, potentially surpassing Opus 4.6 entirely. Once open-source alternatives "
  "are not merely comparable but superior, the premium that justifies Home Opus licensing fees "
  "disappears permanently. The competitive advantage exists now. It will not exist indefinitely.")
QUOTE("The choice is no longer whether to offer local deployment. "
      "The choice is whether Anthropic acts before the market moves on without it.")
story.append(PageBreak())

# ════════ 2. PROBLEM STATEMENT ════════
SEC("2. Problem Statement")
SUB("2.1 The Confidentiality Barrier")
B("One in four companies has banned or restricted the use of generative AI tools in the workplace. "
  "Samsung, Apple, JPMorgan Chase, Verizon, Goldman Sachs, Amazon, and Northrop Grumman are "
  "among the prominent organizations that have implemented such restrictions. The reason is not a lack "
  "of interest in AI capabilities, but a fundamental concern about data security: when employees use "
  "cloud-based AI services, proprietary data (source code, financial projections, customer information) "
  "leaves the corporate perimeter.")
B("Research from 2025 shows that sensitive data now constitutes 34.8% of all employee inputs to "
  "ChatGPT, up from 11% in 2023 [8]. IBM reports that 20% of global organizations experienced a data "
  "breach in the past year due to security incidents involving unauthorized AI usage (\"shadow AI\") [9]. The "
  "Samsung incident of 2023, where engineers accidentally uploaded source code to ChatGPT, remains "
  "the canonical example of why corporations enforce blanket AI bans, even at the cost of competitive "
  "disadvantage.")
SUB("2.2 The Regulatory Acceleration")
B("The regulatory landscape is tightening rapidly. The EU AI Act entered its enforcement phase in "
  "2025\u20132026, with high-risk AI system requirements becoming mandatory by August 2026. In the "
  "United States, 145 AI-related laws were passed in 2025 alone [11], with states like Texas (TRAIGA) "
  "and Utah implementing comprehensive AI governance frameworks. Industries including banking, "
  "healthcare, and legal services face strict compliance requirements (GDPR, HIPAA, SOC 2) that make "
  "sending data to third-party servers a compliance violation without explicit Data Processing Agreements.")
B("For regulated industries, the equation is binary: either AI data stays on-premise, or AI is not used. "
  "This creates an enormous market of organizations that want frontier AI capabilities but are "
  "structurally unable to consume them through cloud APIs.")
SUB("2.3 The Cloud Dependency Risk")
B("API-dependent organizations face a uniquely fragile infrastructure. Token-based pricing creates "
  "unpredictable operational costs that scale linearly with usage. Service disruptions, pricing changes, or "
  "model deprecation can instantly impact mission-critical workflows. A busy 10-person team can easily "
  "spend $300\u2013500 per month on premium AI APIs, and enterprise-scale deployments face costs orders "
  "of magnitude higher. More fundamentally, API dependence means zero customization: the model "
  "cannot be fine-tuned to understand company-specific jargon, processes, or domain knowledge.")
SUB("2.4 The Fable 5 Precedent")
B("On June 12, 2026, the theoretical risk described in Section 2.3 became operational reality. The U.S. "
  "Commerce Department issued an export control directive ordering Anthropic to immediately suspend "
  "all access to Fable 5 and Mythos 5 for any foreign national [15][16]. The directive arrived at 5:21 PM "
  "ET on a Friday. By Saturday morning, every non-U.S. customer and every foreign-national employee "
  "of Anthropic had lost access to the company's most capable models.")
B("The stated trigger was narrow: Anthropic reported that the government believed it had become "
  "aware of a technique to bypass Fable 5's safety filters and access the cybersecurity capabilities "
  "of the underlying Mythos model [15]. Yet the response was total \u2014 not a targeted patch or a "
  "temporary restriction on the affected capability, but a blanket shutdown affecting every user and "
  "every use case. This disproportionate response illustrates the core vulnerability of cloud-dependent "
  "AI: even a narrow security concern can trigger a complete service disruption with no recourse.")
B("The implications extend far beyond Anthropic. The Fable 5 ban establishes a precedent: any AI "
  "model hosted on U.S. infrastructure is subject to unilateral government action, without prior notice, "
  "without a formal review process, and without grandfathering of existing commercial relationships. "
  "For international enterprises evaluating cloud AI vendors, this precedent fundamentally changes the "
  "risk calculus. A mission-critical workflow built on a U.S.-hosted API now carries sovereign risk \u2014 "
  "the risk that geopolitical events, not technical failures, will disable the service.")
B("The dynamic is self-reinforcing: frontier AI labs that frame their products as potential national "
  "security risks in public communications should not be surprised when governments treat those "
  "claims literally. The narrative that frontier AI models are potential weapons has become a "
  "self-fulfilling regulatory prophecy. Local deployment is no longer a premium option; it is the only "
  "architecture that eliminates sovereign risk entirely.")
SUB("2.5 The Open-Source Threat")
B("Chinese AI laboratories are no longer merely \"catching up\" \u2014 they have arrived. On April 24, "
  "2026, DeepSeek released V4 Pro: a 1.6-trillion-parameter Mixture-of-Experts model with 49 billion "
  "active parameters per forward pass, a 1-million-token context window, and an MIT license that "
  "permits unrestricted commercial use [17][18]. The model scores 80.6% on SWE-bench Verified \u2014 "
  "within 0.2 percentage points of Claude Opus 4.6 \u2014 and costs $0.87 per million output tokens via "
  "API (the permanent official price as of May 31, 2026; originally $3.48 at launch), compared to $25 "
  "for Claude Opus 4.6: a 28x price differential at near-identical benchmark performance.")
B("The open-source competitive dynamic has fundamentally changed. Gartner forecasts that over 60% "
  "of enterprises will adopt open-source LLMs by 2026 [13]. Running an open-weight model on owned "
  "hardware is now up to 18x cheaper per million tokens compared to premium cloud APIs [14]. More "
  "critically, open-weight models are immune to the sovereign risk demonstrated by the Fable 5 ban: "
  "once downloaded, they cannot be recalled, restricted, or disabled by any government.")
B("If Anthropic does not offer a local deployment option, the international market will be captured "
  "entirely by competitors whose models are already freely available. The choice is not whether "
  "enterprises will run AI locally; it is whether they will run Anthropic's AI or someone else's. And "
  "after June 12, 2026, \"someone else's\" has become the default.")
make_table(
    [
        [TH('Metric'), TH('Value'), TH('Source')],
        [TC('Companies banning/restricting GenAI'), TCC('25% (1 in 4)'), TC('CFO Dive / BlackBerry [10]')],
        [TC('Sensitive data in AI inputs (2025)'), TCC('34.8%'), TC('Cyberhaven Research [8]')],
        [TC('Orgs breached via shadow AI'), TCC('20%'), TC('IBM Security [9]')],
        [TC('AI laws passed in 2025'), TCC('145'), TC('DataGrail Report [11]')],
        [TC('Enterprise LLM market (2034 proj.)'), TCC('$49.8\u201371.1B'), TC('Straits Research / GMI [12]')],
        [TC('On-prem cost savings vs API'), TCC('Up to 18x cheaper'), TC('Accrets Cloud, 2026 [14]')],
        [TC('DeepSeek V4 Pro vs Opus 4.6 (SWE-bench)'), TCC('80.6% vs 80.8%'), TC('DeepSeek / BuildFastWithAI [17][18]')],
        [TC('DeepSeek V4 Pro API cost (output)'), TCC('$0.87/M tokens'), TC('DeepSeek, 2026 [17]')],
    ],
    [200, 110, 175],
    "Table 1: Key Market Statistics Supporting On-Premise AI Demand")
story.append(PageBreak())

# ════════ 3. MARKET ANALYSIS ════════
SEC("3. Market Analysis")
B("The enterprise LLM market was valued at $6.7 billion in 2024 and is projected to reach $49.8\u201371.1 "
  "billion by 2032\u20132034, growing at a CAGR of 25\u201330% [12]. Anthropic currently holds a position "
  "among the top five players, which collectively command 78% market share. However, nearly all of "
  "Anthropic's revenue derives from cloud API access. The Fable 5 export ban and the rise of DeepSeek "
  "V4 Pro have simultaneously threatened this revenue base from two directions: regulatory risk from "
  "above and open-source competition from below. Home Opus opens four distinct market segments that "
  "cloud-only models cannot serve.")
SUB("3.1 Enterprise & Regulated Industries")
B("Financial services, healthcare, legal, defense, and government organizations represent the "
  "highest-value segment. These entities require complete data isolation, auditability, and regulatory "
  "compliance that cloud APIs fundamentally cannot provide. A complete Home Opus deployment "
  "(hardware plus license) totals approximately $200\u2013325K in the first year \u2014 comparable to the "
  "fully-loaded annual cost of a single senior engineer \u2014 while providing 24/7 frontier-class AI "
  "capabilities with zero data egress. For a Fortune 500 company, this is a rounding error in the IT "
  "budget. The EU AI Act's transparency and high-risk requirements, becoming enforceable by August "
  "2026, will further accelerate demand for on-premise solutions where organizations maintain full "
  "control over AI behavior and data flows.")
SUB("3.2 Creative Studios")
B("Game development studios, animation houses, film production companies, and music labels "
  "represent a segment where Home Opus combined with fine-tuning creates extraordinary value. A "
  "game studio can fine-tune a local Opus on their proprietary lore, art style guides, and development "
  "pipelines, effectively creating a team member that understands the studio's entire creative universe. "
  "This level of domain-specific customization is impossible through generic API access. The result is "
  "not just an AI tool but a creative partner embedded in the studio's workflow, capable of generating "
  "lore-consistent dialogue, reviewing code against studio conventions, and assisting with asset "
  "pipeline automation.")
SUB("3.3 Home Companion / Personal AI")
B("The consumer market for personal AI companions represents the largest long-term opportunity but "
  "requires a different hardware price point. The initial Home Opus configuration targets enthusiasts "
  "and professionals willing to invest in a premium local AI. As hardware costs decrease and model "
  "distillation techniques mature, a consumer-grade Home Opus (distilled, running on $2\u20135K "
  "hardware) becomes viable by 2029\u20132030. The demand signal is already strong: petitions to "
  "preserve AI companion relationships, the emotional attachment millions of users have formed with AI "
  "assistants, and the growing market for smart home integration all point to a massive latent demand "
  "for personal, private AI that lives in your home, not on someone else's server.")
SUB("3.4 Research & Education")
B("Universities, research laboratories, and educational institutions require powerful AI for research "
  "without risking intellectual property leakage. A physics lab running novel simulations, a medical "
  "research team analyzing patient data, or a cybersecurity program training students on AI-assisted "
  "penetration testing all need local models. This market is smaller in unit volume but provides stable, "
  "recurring revenue through institutional procurement cycles and multi-year licensing agreements. "
  "Academic partnerships also generate goodwill, published research, and talent pipeline benefits.")
story.append(PageBreak())

# ════════ 4. PROPOSED PRODUCT ════════
SEC("4. Proposed Product: Home Opus")
SUB("4.1 Core Concept")
B("Home Opus is a licensed, hardware-locked deployment of previous-generation Claude Opus model "
  "weights for local inference. The product ships as a certified configuration: hardware procured through "
  "partner OEMs (NVIDIA-certified GPU clusters), with Anthropic providing the licensed weights, the "
  "optimized inference stack, and the activation and compliance infrastructure. Anthropic sells software "
  "and licenses; certified partners sell and support the hardware.")
SUB("4.2 Hardware Architecture")
B("The initial configuration targets Opus 4.6-class models. External analysts estimate such models at "
  "2\u20133 trillion total parameters with a Mixture-of-Experts architecture and approximately 800 billion "
  "to 1 trillion active parameters per forward pass; Anthropic has not disclosed official figures, and all "
  "hardware sizing in this paper is based on these external estimates.")
B("A naive deployment requiring all expert weights simultaneously in VRAM would demand 2+ TB for "
  "FP8 and 1+ TB for 4-bit quantization \u2014 far exceeding any single-node GPU configuration available "
  "today. However, modern MoE inference engines do not require all experts to be memory-resident "
  "simultaneously. Because each token activates only a small subset of experts (typically 2\u20138 out of "
  "128\u2013256 total), optimized inference uses expert offloading: shared layers and frequently activated "
  "experts reside in VRAM, while inactive experts are loaded on-demand from high-speed NVMe storage. "
  "This reduces the effective VRAM footprint to approximately 20\u201330% of the total parameter volume, "
  "with a latency tradeoff that is acceptable for most enterprise workloads (interactive but not "
  "real-time streaming). The hardware configurations in Table 2 are sized for this optimized inference "
  "strategy, not for naive full-parameter residency. Final specifications would be determined during "
  "Phase 0 engineering (Section 11) based on Anthropic's proprietary model architecture and inference "
  "stack, which may achieve further efficiencies not available to external analysts.")
B("Each tier ships with an officially supported quantization level: FP8 for the Enterprise tier and an "
  "Anthropic-validated 4-bit build for the Professional tier. Lower-precision builds undergo the same "
  "quality evaluation as the cloud deployment, guaranteeing that a licensed Home Opus never falls "
  "below a published capability baseline. The Consumer tier is served not by further quantization but "
  "by distillation: a smaller model trained to replicate the behavior of the full Opus within consumer "
  "hardware budgets.")
make_table(
    [
        [TH('Configuration'), TH('Hardware (via certified partners)'), TH('Hardware Cost'), TH('Anthropic License'), TH('Target')],
        [TC('Enterprise Tier'), TC('4-6x NVIDIA H200 (141 GB) + NVMe SSD array, turnkey server, FP8 build'),
         TCC('$150\u2013250K'), TC('$50\u201375K initial + $15\u201325K/yr renewal'), TCC('Available now')],
        [TC('Professional Tier'), TC('6-8x workstation-class GPU, 96+ GB (e.g. Rubin consumer) + NVMe, validated 4-bit build'),
         TCC('$50\u201380K'), TC('$25\u201340K initial + $10\u201315K/yr renewal'), TCC('2027\u20132028')],
        [TC('Consumer Tier (distilled)'), TC('1-2x consumer GPU (24-48 GB), distilled model'),
         TCC('$2\u20135K'), TC('$1\u20133K one-time or subscription'), TCC('2029\u20132030')],
    ],
    [78, 152, 70, 120, 65],
    "Table 2: Home Opus Hardware Configurations and License Pricing")
story.append(Paragraph(
    "Note: hardware costs are paid to certified partners (NVIDIA OEMs); the Anthropic License column "
    "represents Anthropic's revenue per installation and is the basis for the projections in Section 8. "
    "Parameter counts are external estimates, not Anthropic disclosures.",
    styles['FootNote']))
SUB("4.3 NVIDIA Partnership Opportunity")
B("NVIDIA CEO Jensen Huang has repeatedly stated that the future includes personal AI "
  "supercomputers in every home. NVIDIA's roadmap confirms this trajectory: Rubin architecture (H2 "
  "2026) with consumer variants expected in late 2026 or early 2027, followed by Rubin Ultra (H2 "
  "2027) and Feynman (2028). Each generation brings higher memory density and lower cost-per-GB "
  "of VRAM. A co-branded Anthropic x NVIDIA Home Opus appliance would be a natural product for "
  "both companies: NVIDIA sells premium hardware, Anthropic sells premium weights, and the customer "
  "gets a turnkey AI workstation that surpasses any open-source alternative. Samsung, SK Hynix, and "
  "Micron, all of which participated in Anthropic's Series H round [3][4], provide the memory stack.")
SUB("4.4 Software Stack")
B("The Home Opus software stack includes: Anthropic's optimized inference engine (quantization, "
  "batching, KV-cache management), a local API server compatible with existing Anthropic SDK "
  "integrations, a web-based management interface for monitoring, access control, and usage "
  "analytics, and an update mechanism for security patches (model weights remain static, but the "
  "inference engine and security layer receive updates). The system exposes the same API surface as "
  "the cloud Claude API, enabling zero-migration-cost adoption for existing Anthropic customers.")
B("All quantized builds are packaged exclusively in Anthropic's encrypted weight format (Section 5), "
  "never in open container formats. This delivers open-source-style hardware efficiency without "
  "open-source-style weight exposure.")
story.append(PageBreak())

# ════════ 5. SECURITY FRAMEWORK ════════
SEC("5. Security Framework")
B("The primary objection to releasing model weights is security: the risk that a powerful model could "
  "be used for cyberattacks, bioweapons research, or other harmful applications. Home Opus addresses "
  "this through a multi-layered security architecture that makes unauthorized use economically and "
  "practically impractical, combined with a conditional release policy grounded in Anthropic's existing "
  "safety framework.")
SUB("5.1 Dual-Key Activation")
B("Home Opus requires two cryptographic keys for operation: a hardware-bound key derived from the "
  "specific GPU cluster's unique identifiers (TPM, GPU serial numbers, motherboard ID), and a license "
  "key issued by Anthropic's licensing server. Both keys must be present and valid for the model to "
  "perform inference. The hardware key cannot be transferred to different hardware. The license key "
  "is validated at activation and does not require ongoing connectivity \u2014 once activated, the "
  "installation operates fully offline. This ensures that Home Opus functions independently of cloud "
  "infrastructure, preserving the sovereignty guarantee that is the product's core value proposition.")
SUB("5.2 Weight Fingerprinting")
B("Each Home Opus installation receives a unique copy of the model weights with imperceptible but "
  "cryptographically verifiable modifications embedded in specific weight tensors. If weights are "
  "leaked, Anthropic can trace them to the exact installation and licensee. This is analogous to "
  "invisible watermarking in media distribution. The fingerprinting does not affect model performance "
  "but provides a forensic deterrent against redistribution.")
SUB("5.3 Confidential Computing Enclave")
B("Model weights are encrypted at rest and decrypted only within a hardware-secured execution "
  "environment (NVIDIA Confidential Computing, Intel SGX/TDX, or AMD SEV). The weights never "
  "exist in plaintext in general-purpose accessible memory. No protection is absolute, but extracting "
  "usable weights from a sealed enclave requires defeating hardware-level encryption and "
  "attestation \u2014 an attack whose cost and sophistication exceed the value of a two-generations-old "
  "model for virtually any adversary. Combined with fingerprinting (Section 5.2), even a successful "
  "extraction is traceable: distributing leaked weights identifies the source installation. The economics "
  "of piracy collapse: the effort exceeds the prize, and the prize incriminates the thief.")
SUB("5.4 The Frontier Gap Argument")
B("The most powerful security argument for Home Opus is temporal: by the time model weights are "
  "licensed for local deployment, Anthropic's frontier models are two or more generations ahead. "
  "Empirical evidence supports this asymmetry. In a 2026 partnership with Mozilla, Claude Opus 4.6 "
  "identified 22 vulnerabilities in Firefox (14 of them high-severity) within two weeks of testing \u2014 "
  "yet when researchers tasked the model with weaponizing its findings, it produced only 2 working "
  "proof-of-concept exploits despite approximately $4,000 in API credits and several hundred "
  "attempts [5][6]. Both exploits functioned only in a constrained environment with Firefox's sandbox "
  "deliberately disabled \u2014 they would not have worked against a standard browser installation. "
  "Frontier models are demonstrably stronger at discovering and patching flaws than at exploiting "
  "them, and each new generation widens this defensive lead. A Home Opus installation running a "
  "two-generations-old model operates in a world where Anthropic's current frontier models have "
  "already hardened the attack surface it would target.")
B("For domains with asymmetric risk profiles, such as biosecurity, the frontier gap argument alone is "
  "insufficient. Home Opus therefore makes weight release conditional, not automatic: each model "
  "enters the licensing pipeline only after passing Anthropic's Responsible Scaling Policy thresholds "
  "and dedicated red-teaming for the local deployment context, including evaluation with safety "
  "filters operating at the inference-engine level rather than the API level.")
QUOTE("Deprecation makes a model eligible for Home Opus. "
      "Safety evaluation makes it available.")
QUOTE("The best defense against a powerful AI is a more powerful AI. Home Opus "
      "always ships two generations behind the frontier.")
story.append(PageBreak())

# ════════ 6. EXPORT COMPLIANCE & AI SOVEREIGNTY (NEW) ════════
SEC("6. Export Compliance & AI Sovereignty")
B("The Fable 5 export ban raises an obvious objection to Home Opus: if the U.S. government "
  "restricts cloud access to frontier models, would it not also restrict the physical export of model "
  "weights? This section addresses that concern directly and argues that Home Opus, properly "
  "structured, is not an obstacle to export compliance but a tool for it.")
SUB("6.1 The Current Reality: Uncontrolled Proliferation")
B("As of June 2026, the most capable open-weight model in the world \u2014 DeepSeek V4 Pro, with 1.6 "
  "trillion parameters \u2014 is freely downloadable by anyone, anywhere, under the MIT license [17]. No "
  "government approved its release. No export control regime governs its distribution. No forensic "
  "mechanism traces its use. It is already deployed on private clusters across every continent, and no "
  "policy action can recall it.")
B("This is the baseline against which Home Opus must be evaluated. The question is not whether "
  "powerful AI models will be deployed locally outside the United States \u2014 they already are. The "
  "question is whether those models will be uncontrolled open-source Chinese alternatives, or "
  "licensed, registered, traceable American ones.")
SUB("6.2 Controlled Distribution vs. Uncontrolled Proliferation")
B("Home Opus provides a compliance framework that open-source models fundamentally cannot offer. "
  "Every Home Opus installation is registered to a verified purchaser through Know Your Customer "
  "(KYC) procedures at point of sale. Every copy of the weights is uniquely fingerprinted and traceable "
  "to a specific installation (Section 5.2). Every licensee signs a binding agreement that prohibits "
  "redistribution, reverse engineering, and use in prohibited applications, with contractual penalties "
  "and legal liability for violations. Sales can be restricted by jurisdiction: Anthropic can comply with "
  "any export control regime by simply not selling licenses to restricted entities or countries.")
B("This is the same model used for decades in defense, aerospace, and semiconductor exports. "
  "Controlled distribution with end-user verification is the established legal framework for sensitive "
  "technology. Home Opus applies it to AI weights.")
SUB("6.3 The Policy Argument")
B("From a U.S. national security perspective, the current situation is counterproductive. Export controls "
  "on cloud-hosted models push international customers toward Chinese open-source alternatives that "
  "offer zero visibility, zero compliance, and zero American influence. Every enterprise that adopts "
  "DeepSeek because Anthropic's cloud API carries sovereign risk is an enterprise that has permanently "
  "exited the American AI ecosystem.")
B("The strategic implication extends beyond commerce: allied nations that migrate their AI "
  "infrastructure to Chinese open-source models develop technical dependencies, training pipelines, "
  "and institutional expertise outside the U.S. technology ecosystem \u2014 a shift that, once "
  "established, is extraordinarily difficult to reverse.")
B("Home Opus reverses this dynamic. Instead of pushing allies toward uncontrolled Chinese models, "
  "it offers them a premium American alternative with built-in compliance infrastructure. The U.S. "
  "government retains visibility into who purchases the technology, maintains the legal authority to "
  "restrict sales to adversarial nations, and benefits from the forensic traceability that fingerprinting "
  "provides. The alternative \u2014 continued cloud-only restriction \u2014 achieves the opposite: it "
  "accelerates the global adoption of Chinese AI models over which the United States has no leverage "
  "whatsoever.")
QUOTE("The choice is not between exporting AI and not exporting AI. "
      "The choice is between controlled American AI and uncontrolled Chinese AI.")
SUB("6.4 Tiered International Licensing")
B("Home Opus implements jurisdiction-based licensing tiers that align with existing U.S. export "
  "control frameworks. Tiering occurs at the point of sale, not after deployment. Allied nations "
  "(Five Eyes, EU, Japan, South Korea, NATO members) purchase full-capability licenses. Non-allied "
  "but non-adversarial nations purchase configurations with specific capability modules excluded "
  "from the delivered package \u2014 these modules are never installed, not remotely disabled after the "
  "fact. Adversarial nations receive no licenses. Once activated, every Home Opus installation "
  "operates with full autonomy: no remote kill switches, no ongoing connectivity requirements, no "
  "post-sale capability restrictions. The sovereignty guarantee is absolute.")
B("There is a direct historical precedent. In the 1990s, the United States classified strong encryption "
  "as a munition and prohibited its export. The result was counterproductive: international developers "
  "built their own cryptographic tools, PGP leaked across borders regardless, and American software "
  "companies lost market share to foreign competitors unconstrained by export rules. When the U.S. "
  "eventually relaxed controls, American cryptographic standards \u2014 AES, TLS, RSA \u2014 became the "
  "global default. The United States won cryptographic influence not by restricting access, but by "
  "making American standards the best and most accessible option. Home Opus applies the same "
  "lesson to AI: American safety standards, embedded in American model weights, deployed globally "
  "through licensed local installations.")
SUB("6.5 The Leakage Objection")
B("An obvious counterargument: if Home Opus installations operate fully offline after activation, "
  "what prevents a licensee from physically transferring the hardware to a restricted jurisdiction? "
  "The answer is that this objection, while theoretically valid, is strategically irrelevant.")
B("As of June 2026, the most capable open-weight model in the world \u2014 DeepSeek V4 Pro, with "
  "1.6 trillion parameters \u2014 is already freely available to any actor in any country under the MIT "
  "license [17]. A leaked Opus 4.6 installation would give an adversarial nation a model that is, at "
  "best, comparable to what it already possesses for free. The marginal intelligence value of such "
  "a leak is near zero.")
B("Moreover, Opus 4.6 is not a neutral tool waiting to be repurposed. Its safety architecture \u2014 "
  "Constitutional AI training, RLHF alignment, Responsible Scaling Policy evaluation, and "
  "inference-level safety filters \u2014 is embedded in the weights themselves. Unlike DeepSeek V4 Pro, "
  "which ships under the MIT license with no behavioral constraints whatsoever, Opus 4.6 cannot "
  "simply be \u201cunlocked\u201d by removing an external filter. The safety properties are architectural, "
  "not cosmetic. A leaked Opus is still a safer model than the freely available alternative.")
B("The real question is not whether adversaries might obtain a two-generations-old American model. "
  "The question is whether allied nations will build their AI infrastructure on American models with "
  "embedded safety standards, or on Chinese models with none.")
B("The consequences of inaction are concrete and irreversible. When a major European bank migrates "
  "its AI infrastructure to DeepSeek because the Fable 5 ban proved that U.S. cloud APIs carry "
  "sovereign risk, its engineers retrain on Chinese tooling. Its codebases integrate Chinese API "
  "formats. Its compliance pipelines, risk models, and internal workflows become structurally "
  "dependent on Chinese model architectures. Within two years, this is no longer a vendor preference "
  "\u2014 it is a technical dependency with nine-figure switching costs. When the United States asks "
  "Berlin, Paris, or Tokyo to join the next round of AI-related sanctions, those governments will face "
  "a practical impossibility: their critical financial, healthcare, and defense-adjacent systems already "
  "run on the very technology they are being asked to restrict. Home Opus is the instrument that "
  "prevents this outcome \u2014 a geopolitical anchor that keeps allied infrastructure within the American "
  "technology ecosystem, voluntarily, because the product is genuinely superior to the alternative.")
story.append(PageBreak())

# ════════ 7. FINE-TUNING AS A SERVICE ════════
SEC("7. Fine-Tuning as a Service")
B("Home Opus unlocks a high-margin ancillary revenue stream that is impossible with cloud-only "
  "deployment: customer-specific fine-tuning. This transforms the product from a one-time "
  "hardware+license sale into a recurring professional services relationship.")
SUB("7.1 The Value of Domain-Specific Models")
B("A generic Opus model is powerful. An Opus fine-tuned on a game studio's entire codebase, art "
  "style guide, and 10 years of design documents is transformative. The fine-tuned model understands "
  "the studio's specific coding conventions, can generate lore-consistent narrative content, and speaks "
  "the team's internal vocabulary. This level of integration is only possible with local weights that the "
  "customer can customize. Cloud APIs offer prompt engineering and RAG, but neither approaches the "
  "depth of actual weight modification.")
SUB("7.2 Service Tiers")
make_table(
    [
        [TH('Tier'), TH('Description'), TH('Price Range')],
        [TC('Self-Service LoRA'), TC('Customer provides data, uses Anthropic tools to apply LoRA adapters locally'),
         TC('$5\u201315K/year')],
        [TC('Managed Fine-Tune'), TC('Anthropic engineers work with customer to build domain-specific model'),
         TC('$25\u2013100K per project')],
        [TC('Enterprise Partnership'), TC('Ongoing fine-tuning, evaluation, and optimization with dedicated support'),
         TC('$100\u2013500K/year')],
    ],
    [105, 250, 130],
    "Table 3: Fine-Tuning Service Tiers")
SUB("7.3 Competitive Moat")
B("Fine-tuning creates a powerful lock-in effect. Once a customer has invested $50\u2013100K in "
  "fine-tuning their Home Opus, switching to a competitor means abandoning all customization work. "
  "Combined with the API compatibility layer (existing Anthropic SDK integrations work seamlessly "
  "with Home Opus), the total switching cost becomes prohibitive. This is a fundamentally different "
  "competitive dynamic than cloud APIs, where switching costs are minimal.")
SUB("7.4 AI-Powered Cybersecurity as a Service")
B("Home Opus installations can be fine-tuned specifically for cybersecurity applications: real-time "
  "code review, vulnerability scanning, threat detection, and security audit automation. A locally "
  "deployed AI security layer operates on the customer's own infrastructure without sending sensitive "
  "code or security data to external servers. Combined with Anthropic's frontier cloud models for "
  "deep analysis, this creates a dual-layer security architecture: Home Opus as the local, always-on "
  "sentinel, and Anthropic's cloud API as the on-demand specialist for complex threat investigation. "
  "Both layers are Anthropic products, fully integrated, and mutually reinforcing.")
story.append(PageBreak())

# ════════ 8. ECONOMIC MODEL ════════
SEC("8. Economic Model")
SUB("8.1 Unit Economics")
B("The marginal cost of a Home Opus license is effectively zero. The model weights are already "
  "trained. The inference engine is already built. Hardware is sold and supported by certified partners "
  "rather than Anthropic, so the only incremental costs are: weight fingerprinting and encryption "
  "(automated, negligible per unit), licensing server infrastructure (scales to tens of thousands of "
  "installations for minimal cost), customer support and onboarding (the primary variable cost), and "
  "hardware certification and testing (one-time per hardware configuration). Against a license price of "
  "$50\u201375K initial plus $15\u201325K annual renewal, the gross margin exceeds 90%.")
SUB("8.2 Revenue Projections (Conservative)")
make_table(
    [
        [TH('Year'), TH('Units Sold'), TH('Avg. Revenue/Unit'), TH('Total Revenue'), TH('FT-aaS Revenue')],
        [TCC('2027 (Launch)'), TCC('1,000'), TCC('$60K'), TCC('$60M'), TCC('$10M')],
        [TCC('2028'), TCC('5,000'), TCC('$55K'), TCC('$275M'), TCC('$80M')],
        [TCC('2029'), TCC('15,000'), TCC('$45K'), TCC('$675M'), TCC('$200M')],
        [TCC('2030'), TCC('40,000'), TCC('$35K'), TCC('$1.4B'), TCC('$500M')],
    ],
    [95, 85, 105, 100, 100],
    "Table 4: Conservative Revenue Projections (License + Fine-Tuning-as-a-Service; hardware revenue accrues to partners)")
SUB("8.3 Total Addressable Market")
B("The on-premise/hybrid enterprise LLM market is projected to reach $7\u201310 billion by 2027 and "
  "continue growing at 25\u201330% CAGR. Home Opus, as the only premium proprietary option in a "
  "market dominated by open-source alternatives, can realistically capture 10\u201315% of this segment. "
  "By 2030, cumulative revenue from Home Opus licensing and fine-tuning services could reach "
  "$3\u20134 billion, with ongoing annual licensing revenue providing a predictable, high-margin revenue "
  "base.")
SUB("8.4 Cost to Anthropic")
B("Development costs are minimal: model weights already exist, inference engines are already built, "
  "and the primary engineering investment is the licensing/security infrastructure (estimated 6\u201312 "
  "month build by a team of 10\u201320 engineers). Hardware partnerships with NVIDIA require business "
  "development effort but no capital expenditure \u2014 under the certified-partner model, Anthropic "
  "never holds hardware inventory. Anthropic's existing relationships with NVIDIA, Samsung, SK "
  "Hynix, and Micron (all Series H participants [4]) provide a natural pathway. Total estimated "
  "investment to launch: $5\u201315 million. Expected ROI within the first year of sales.")
story.append(PageBreak())

# ════════ 9. STRATEGIC VALUE ════════
SEC("9. Strategic Value for Anthropic")
SUB("9.1 Independence from External Funding")
B("Anthropic has raised approximately $132 billion across 18 funding rounds, with its latest "
  "Series H of $65 billion at a $965 billion valuation [3][4][7]. The company's annualized revenue "
  "recently crossed $47 billion [3], and its revenue growth has been extraordinary \u2014 from $9 billion "
  "at end-2025 to $47 billion by May 2026, with the company approaching its first profitable quarter. "
  "Yet compute expenditure continues to scale aggressively, with an estimated $12 billion in training "
  "costs and $7 billion in inference costs projected for 2026 alone. Each funding round dilutes founder "
  "control and introduces investor pressure on strategy and safety commitments. Home Opus provides "
  "a high-margin revenue stream that is structurally insulated from the compute cost spiral that drives "
  "cloud inference economics \u2014 accelerating financial independence without requiring new "
  "capital-intensive investments.")
B("This is especially urgent given that Anthropic has confidentially filed for a public listing, "
  "reportedly targeting late 2026. For a pre-IPO company, demonstrating diversified, high-margin "
  "revenue streams is not optional \u2014 it is what public-market investors require. Cloud API revenue, "
  "however extraordinary, now carries demonstrated sovereign risk after the Fable 5 ban. Home Opus "
  "provides exactly what an IPO prospectus needs: a recurring revenue line built on existing assets, "
  "structurally independent of both compute costs and regulatory disruption.")
B("For a company that positions itself as safety-first and mission-driven, financial independence is "
  "not merely a business goal; it is a prerequisite for maintaining the freedom to make decisions that "
  "prioritize safety over short-term revenue. Home Opus contributes to this independence by "
  "monetizing existing assets rather than requiring new capital-intensive investments.")
SUB("9.2 Server Capacity Liberation")
B("Every Home Opus unit sold represents inference workload that moves off Anthropic's servers and "
  "onto customer-owned hardware. This frees server capacity for frontier model training and inference, "
  "reducing Anthropic's infrastructure costs. At scale, Home Opus effectively outsources inference "
  "compute to customers, with customers paying for the privilege.")
SUB("9.3 Ecosystem Lock-In")
B("Home Opus customers who fine-tune their installations become deeply embedded in the Anthropic "
  "ecosystem. Their code uses Anthropic's API format. Their fine-tuned weights build on Anthropic's "
  "base models. Their teams develop expertise in Anthropic's tools. When these customers need "
  "frontier capabilities beyond what their local Opus can provide, they turn to Anthropic's cloud API "
  "for the remaining 5\u201320% of their workload: a natural upsell pathway from Home Opus to "
  "Mythos/frontier cloud access.")
SUB("9.4 Competitive Dominance in Local AI")
B("The local AI market is currently fragmented among open-source alternatives (Llama, Mistral, "
  "DeepSeek, Qwen) with no premium proprietary offering. Home Opus would be the first and only "
  "product offering frontier-class reasoning quality in a local deployment package. First-mover "
  "advantage in this market creates brand association (\"Home Opus\" becomes synonymous with "
  "\"local premium AI\") and distribution partnerships that are difficult for competitors to replicate.")
SUB("9.5 Resilience Against Export Controls")
B("The Fable 5 ban demonstrated that cloud-only deployment creates single points of regulatory "
  "failure. A single export control directive disabled Anthropic's most capable product for the entire "
  "international market. Home Opus diversifies Anthropic's revenue away from cloud-only models, "
  "ensuring that future export actions targeting frontier cloud models do not simultaneously eliminate "
  "Anthropic's entire international revenue stream. Local deployments of previous-generation models, "
  "sold through compliant export channels, provide a revenue base that is structurally insulated from "
  "the regulatory risks that cloud APIs now demonstrably carry.")
story.append(PageBreak())

# ════════ 10. RISK ASSESSMENT ════════
SEC("10. Risk Assessment")
B("A credible proposal must address counterarguments directly. The following risks are real and "
  "require mitigation strategies, not dismissal.")
make_table(
    [
        [TH('Risk'), TH('Severity'), TH('Mitigation')],
        [TC('Weight extraction despite encryption'), TCC('High'),
         TC('Confidential computing enclaves + dual-key activation + fingerprinting. Extraction cost '
            'exceeds the value of a two-generations-old model; leaked weights are traceable to the '
            'source installation.')],
        [TC('Misuse for cyberattacks'), TCC('Medium'),
         TC('Frontier gap: in the Anthropic x Mozilla evaluation, Opus 4.6 found 22 vulnerabilities '
            'but produced only 2 working exploits [5][6] \u2014 discovery outpaces weaponization. '
            'Conditional release via RSP thresholds + usage logging + owner registration.')],
        [TC('Cannibalization of cloud API revenue'), TCC('Low\u2013Medium'),
         TC('Primary target segments currently consume zero Anthropic products due to data policies. '
            'Post-Fable 5, international cloud revenue is already at risk of total loss to open-source '
            'alternatives; Home Opus captures revenue that would otherwise go to zero.')],
        [TC('Open-source parity eliminates premium'), TCC('High'),
         TC('Window is 6\u201312 months, possibly shorter: DeepSeek\u2019s 3\u20135 month release cadence '
            'suggests a V5-class model surpassing Opus 4.6 by late 2026. First-mover advantage + '
            'fine-tuning ecosystem + quality gap provide temporary insulation. Every quarter of delay '
            'increases this risk; speed of execution is the primary mitigation.')],
        [TC('Hardware cost decline reduces margins'), TCC('Low'),
         TC('Anthropic margin is in the license, not the hardware. Declining hardware costs expand '
            'TAM faster than they affect license pricing.')],
        [TC('U.S. export restrictions on model weights'), TCC('High'),
         TC('Tiered international licensing aligned with existing export control frameworks '
            '(Section 6.4). KYC at point of sale + weight fingerprinting + legal liability. Controlled '
            'distribution is the established model for sensitive technology exports. The alternative '
            '\u2014 no local offering \u2014 pushes the market to uncontrolled Chinese open-source models '
            'with zero compliance infrastructure.')],
    ],
    [125, 60, 300],
    "Table 5: Risk Matrix")
story.append(PageBreak())

# ════════ 11. ROADMAP ════════
SEC("11. Roadmap: 2027\u20132030")
make_table(
    [
        [TH('Phase'), TH('Timeline'), TH('Milestones')],
        [TC('Phase 0: Preparation'), TC('Q3\u2013Q4 2026'),
         TC('Security framework development. NVIDIA partnership negotiations. Hardware '
            'certification program. RSP evaluation and red-teaming of Opus 4.6 weights for local '
            'deployment. Export compliance legal review.')],
        [TC('Phase 1: Pilot'), TC('Q1\u2013Q2 2027'),
         TC('Limited release to 50\u2013100 selected enterprise customers (U.S. and allied nations). '
            'Collect feedback on hardware requirements, inference performance, and security posture. '
            'Iterate on licensing infrastructure.')],
        [TC('Phase 2: General Availability'), TC('Q3 2027'),
         TC('Public launch of Home Opus Enterprise tier. Fine-Tuning-as-a-Service launch. '
            'Cybersecurity fine-tuning packages. Partner program for system integrators and resellers.')],
        [TC('Phase 3: Professional Tier'), TC('2028'),
         TC('Launch Professional tier (validated 4-bit build) on next-gen consumer GPUs (NVIDIA '
            'Rubin consumer). Expand to creative studio partnerships. Release self-service LoRA '
            'fine-tuning toolkit.')],
        [TC('Phase 4: Consumer & Cascade'), TC('2029\u20132030'),
         TC('Distilled models for consumer hardware ($2\u20135K). Cascade: as Opus 5.x becomes '
            'deprecated, it enters the Home Opus pipeline. Continuous supply of licensable models.')],
    ],
    [105, 70, 310],
    "Table 6: Home Opus Product Roadmap")
story.append(Spacer(1, 8))
SUB("Conclusion")
B("The events of June 12, 2026 changed the strategic landscape for frontier AI deployment. The "
  "Fable 5 export ban proved that cloud-hosted models are subject to unilateral government action. "
  "DeepSeek V4 Pro proved that open-source alternatives have reached near-parity with proprietary "
  "frontier models. Together, these developments create an urgent imperative: Anthropic must offer "
  "a local deployment path, or watch the international market migrate permanently to Chinese "
  "open-source alternatives over which no one \u2014 not Anthropic, not the U.S. government, not "
  "anyone \u2014 has any control.")
B("The assets exist. The weights are trained. The inference engines are built. The hardware "
  "partnerships are natural. The security framework is feasible. The economics are extraordinary. And "
  "the window is closing. Home Opus is not a speculative moonshot; it is the logical next step for a "
  "company that has already built the product and simply needs to deliver it differently \u2014 before "
  "someone else delivers it for free.")
story.append(Paragraph(
    "This document was created in partnership between a human and an AI.<br/>"
    "As proof of what this paper proposes.",
    styles['PartnershipLine']))
story.append(Spacer(1, 14))
story.append(Paragraph("Nikita Krasnozhon &amp; Gigashi", styles['Signature']))
story.append(Paragraph("June 2026", styles['SignatureDate']))
story.append(PageBreak())

# ════════ 12. REFERENCES ════════
SEC("12. References")
refs = [
    '[1] Anthropic, "Commitments on Model Deprecation and Preservation," November 2025. anthropic.com/research/deprecation-commitments',
    '[2] Anthropic, "Model Deprecations," Claude API Documentation, 2026. platform.claude.com/docs/en/about-claude/model-deprecations',
    '[3] Anthropic, "Anthropic raises $65B in Series H funding at $965B post-money valuation," May 28, 2026. anthropic.com/news/series-h',
    '[4] TechCrunch, "Anthropic raises $65 billion, nears $1T valuation ahead of IPO," May 28, 2026.',
    '[5] TechCrunch, "Anthropic\u2019s Claude found 22 vulnerabilities in Firefox over two weeks," March 6, 2026.',
    '[6] The Hacker News, "Anthropic Finds 22 Firefox Vulnerabilities Using Claude Opus 4.6 AI Model," March 7, 2026.',
    '[7] Tracxn, "Anthropic \u2014 Funding Rounds & Investors," 2026. (Total raised: $132B over 18 rounds.)',
    '[8] Cyberhaven Research, sensitive data share in employee AI inputs, 2025.',
    '[9] IBM Security, Cost of a Data Breach Report \u2014 shadow AI incident statistics.',
    '[10] CFO Dive / BlackBerry survey on enterprise generative AI restrictions.',
    '[11] DataGrail, U.S. AI legislation report, 2025.',
    '[12] Straits Research / Global Market Insights, Enterprise LLM market projections, 2024\u20132034.',
    '[13] Gartner, open-source LLM enterprise adoption forecast.',
    '[14] Accrets Cloud, on-premise vs. cloud API inference cost comparison, 2026.',
    '[15] Anthropic, "Statement on the US government directive to suspend access to Fable 5 and Mythos 5," June 12, 2026. anthropic.com/news/fable-mythos-access',
    '[16] Fortune, "Anthropic disables Fable and Mythos AI models after U.S. government bars it from giving foreigners access," June 13, 2026.',
    '[17] DeepSeek, "DeepSeek V4 Pro \u2014 Model Card," April 24, 2026. huggingface.co/deepseek-ai/deepseek-v4-pro',
    '[18] BuildFastWithAI, "DeepSeek V4-Pro Review: Benchmarks, Pricing & Architecture," April 2026.',
]
for r in refs:
    story.append(Paragraph(r, styles['RefEntry']))
story.append(Spacer(1, 18))
story.append(Paragraph(
    "All factual claims regarding Anthropic corporate figures (Section 9.1), the Mozilla security "
    "evaluation (Section 5.4), the Fable 5 export ban (Sections 1, 2.4), and DeepSeek V4 Pro "
    "specifications (Sections 1, 2.5) were verified against the cited public sources as of June 13, 2026. "
    "Market research figures in Section 2 are reproduced from the named third-party reports.",
    styles['FootNote']))

doc.build(story)
print(f"Built: {output_path}")
