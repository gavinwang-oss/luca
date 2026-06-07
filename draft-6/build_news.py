# -*- coding: utf-8 -*-
"""Generate local news article pages for draft-6 from fetched lucahealthcare.com content.
Each page reuses the draft-6 header (icon sprite + nav) and footer, with an article template.
Run from draft-6/:  python3 build_news.py
"""
import html, os, re

HEADER = open('/tmp/sprite_header.html').read()
FOOTER = open('/tmp/footer.html').read()

# article links in the page point to index.html#x etc; in news/ subdir we must prefix ../
def fix_links(s):
    s = s.replace('href="index.html', 'href="../index.html')
    s = s.replace('href="contact.html', 'href="../contact.html')
    s = s.replace('href="resources.html', 'href="../resources.html')
    s = s.replace('href="#resources"', 'href="../index.html#resources"')
    s = s.replace('href="#company"', 'href="../index.html#company"')
    s = s.replace('href="/"', 'href="../index.html"')
    s = s.replace('src="assets/', 'src="../assets/')
    s = s.replace('href="assets/', 'href="../assets/')
    return s

HEADER_F = fix_links(HEADER)
FOOTER_F = fix_links(FOOTER)

# Body block helpers -> HTML
def H(t):   return f'      <h2 class="art-h">{t}</h2>'
def P(t):   return f'      <p>{t}</p>'
def Q(t, who): return f'      <blockquote class="art-quote">{t}<cite>{who}</cite></blockquote>'
def UL(items): 
    lis = ''.join(f'<li>{i}</li>' for i in items)
    return f'      <ul class="art-list">{lis}</ul>'

PAGE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title_plain} — Luca Healthcare</title>
  <meta name="description" content="{desc}" />
  <link rel="icon" href="../assets/img/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="../assets/img/favicon-32.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="../assets/img/favicon-180.png" />
  <meta name="theme-color" content="#009EDF" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/css/main.css?v=12" />
</head>
<body>

{header}

<main>
  <article class="article">
    <div class="container art-container">
      <a href="../index.html#resources" class="art-back"><svg viewBox="0 0 24 24" style="transform:rotate(180deg)"><use href="#i-arrow"/></svg> Back to news</a>
      <span class="art-tag">{tag}</span>
      <h1 class="art-title">{title}</h1>
      <div class="art-meta">{date}</div>
      <div class="art-lead">{lead}</div>
      <div class="art-body">
{body}
      </div>
    </div>
  </article>
</main>

{footer}

<script src="../assets/js/i18n-dict.js?v=11"></script>
<script src="../assets/js/main.js?v=4"></script>
</body>
</html>
'''

def build(slug, tag, title, date, lead, blocks, desc):
    body = '\n'.join(blocks)
    title_plain = re.sub('<[^>]+>', '', title)
    out = PAGE.format(
        title_plain=html.escape(title_plain),
        desc=html.escape(desc),
        header=HEADER_F, footer=FOOTER_F,
        tag=tag, title=title, date=date, lead=lead, body=body,
    )
    os.makedirs('news', exist_ok=True)
    with open(f'news/{slug}.html', 'w') as f:
        f.write(out)
    print('wrote news/%s.html' % slug)

# ============================ ARTICLES ============================
articles = []

articles.append(dict(
  slug='npj-digital-medicine-publication', tag='Publication',
  title='Luca Healthcare Announces Landmark Publication in Nature npj Digital Medicine: Propelling Respiratory Diagnostics Toward Universal Device-Invariance',
  date='Shanghai — March 2, 2026',
  desc='Luca Healthcare announces a peer-reviewed framework in npj Digital Medicine that uses cough acoustics to achieve 0.96 AUROC in COPD detection.',
  lead='The peer-reviewed framework utilizes cough acoustics to achieve 0.96 AUROC in COPD detection; CEO Echo Chen, PhD, outlines expansion into major chronic and acute respiratory disease pipelines.',
  blocks=[
    P('Luca Healthcare, a global innovator in AI-driven health solutions, today announced the publication of its breakthrough AI research in the high-impact journal <em>npj Digital Medicine</em>. The article, titled &ldquo;A device-invariant multi-modal learning framework for respiratory disease classification,&rdquo; marks a pivotal shift in digital health by solving the &ldquo;hardware hurdle&rdquo;&mdash;ensuring that diagnostic accuracy remains consistent regardless of the smartphone or recording device used.'),
    H('The Primary Breakthrough: Cough as a Clinical Biomarker'),
    P('The publication details a first-of-its-kind AI framework that analyzes cough sounds&mdash;complex bio-acoustic signatures&mdash;to identify respiratory pathologies. Unlike traditional models that are often tethered to specific high-end hardware, Luca&rsquo;s framework employs an <strong>adversarial branch</strong> and <strong>invariant risk minimization (IRM)</strong> to strip away &ldquo;device noise.&rdquo;'),
    P('This allows the AI to extract pure physiological data from any microphone, achieving a superior <strong>0.9698 AUROC for COPD identification</strong>.'),
    H('The Secondary Key: Universal Scalability'),
    P('Historically, &ldquo;device effect&rdquo; has been the primary barrier to the global scaling of digital biomarkers. Luca&rsquo;s framework proves that high-fidelity diagnostics can be delivered via any mobile device, unlocking massive market potential in both developed healthcare systems and low-resource settings.'),
    H('Executive Commentary'),
    Q('&ldquo;Cough sounds are bio-signatures that hold the potential to solve a global respiratory crisis affecting over 750 million people with chronic diseases and over 1 billion with acute infections annually. This publication in <em>Nature npj Digital Medicine</em> is a testament to our success in building a device-invariant foundation. Having validated this framework in COPD, we are now aggressively expanding our pipeline to include other major chronic respiratory diseases and acute infection diagnostics, ensuring our technology serves as a universal &lsquo;digital stethoscope&rsquo; for the 21st century.&rdquo;', 'Echo Chen, PhD, CEO of Luca Healthcare'),
    H('Strategic Roadmap: Beyond COPD'),
    P('While the study highlights gold-standard performance in COPD and Lower Respiratory Tract Infections (LRTI), Luca Healthcare is leveraging this same device-invariant technology to address:'),
    UL([
      '<strong>Chronic Diseases:</strong> Expanding into Asthma, Bronchiectasis, and Pulmonary Fibrosis monitoring',
      '<strong>Decentralized Clinical Trials:</strong> Providing pharmaceutical partners with a standardized, hardware-agnostic tool to measure drug efficacy remotely',
      '<strong>Acute Infections:</strong> Developing rapid screening for Pneumonia and other viral respiratory tract infections',
    ]),
  ],
))

articles.append(dict(
  slug='nmpa-de-novo-coughsearch', tag='Regulatory',
  title='Luca Healthcare&rsquo;s CoughSearch&reg; Receives NMPA De Novo Innovation Designation as a Class III Medical Device',
  date='Shanghai, China — January 10, 2026',
  desc='CoughSearch® becomes the first AI-driven cough-analysis solution for COPD assessment to receive NMPA De Novo Innovation designation.',
  lead='The National Medical Products Administration (NMPA) has granted Luca Healthcare&rsquo;s CoughSearch&reg; &ldquo;COPD Assessment Software&rdquo; a De Novo Innovation designation under China&rsquo;s special review pathway for Class III innovative medical devices.',
  blocks=[
    P('This designation marks a major milestone for Luca Healthcare. CoughSearch&reg; is the <strong>first AI-driven cough-analysis solution for COPD assessment</strong> to receive national-level &ldquo;Innovation Device&rdquo; recognition. The designation also reflects the agency&rsquo;s support for AI and advanced technologies that address real clinical needs and demonstrate clear potential for large-scale adoption.'),
    P('In 2025, fewer than <strong>60 Class III devices</strong> earned admission into China&rsquo;s innovative approval channel, underscoring the extraordinary rigor and exclusivity of this pathway.'),
    H('A National Chronic Disease Priority'),
    P('COPD has become a top priority within China&rsquo;s chronic disease management strategy. Beginning in 2024, COPD was added to the national basic public health program&mdash;joining hypertension and diabetes as the third major chronic disease under standardized management. Implementation efforts continued through 2025, reflecting the urgency of addressing a condition that is now the third leading cause of death in China and globally.'),
    P('A major barrier in COPD management is the limited accessibility of diagnostic tools. Pulmonary function tests (PFTs), the current clinical standard, require specialized equipment, trained personnel, and dedicated space. A single assessment can take more than 20 minutes, making widespread screening and follow-up difficult in primary care and lower-resource settings.'),
    H('Lowering the Barrier to Screening'),
    P('CoughSearch&reg; was developed to lower this barrier. The software enables COPD assessment using a standard smartphone, reducing diagnostic time to <strong>under three minutes</strong> while maintaining high accuracy. In multi-center, prospective clinical studies using PFTs as the gold standard, CoughSearch&reg; achieved <strong>92% sensitivity (95% CI: 86&ndash;96%)</strong> and <strong>89% specificity (95% CI: 84&ndash;92%)</strong>.'),
    P('To ensure real-world robustness, Luca Healthcare built a dataset of more than <strong>30,000 patient samples</strong> across 15 regions, spanning all major respiratory conditions. CoughSearch&reg; is powered by a Transformer-based architecture and enhanced with adversarial learning to maintain performance across diverse devices and acoustic environments. This approach delivers consistent accuracy regardless of smartphone model or recording hardware.'),
    P('Building on this technical foundation, Luca plans to expand into additional respiratory use cases, including AECOPD risk identification, asthma, and upper and lower respiratory tract infections. By enabling low-barrier screening, assessment, and follow-up across a broader range of conditions, Luca aims to improve access to care and advance personalized respiratory medicine.'),
  ],
))

articles.append(dict(
  slug='ats-2026-orlando', tag='Research',
  title='Luca Healthcare Continues Global Momentum with Acceptance to Present Breakthrough AI Research at ATS 2026 in Orlando',
  date='Singapore — December 30, 2025',
  desc='Luca Healthcare&rsquo;s research on sound-based biomarkers for respiratory disease has been accepted for presentation at ATS 2026 in Orlando.',
  lead='Luca Healthcare today announced that its research on sound-based biomarkers for respiratory disease has been accepted for presentation at the American Thoracic Society (ATS) International Conference 2026, taking place May 15&ndash;20, 2026 in Orlando, Florida.',
  blocks=[
    P('This milestone follows Luca&rsquo;s recent recognition at the European Respiratory Society (ERS) Congress 2025, underscoring the company&rsquo;s accelerating global momentum and scientific leadership in acoustic biomarker innovation.'),
    P('The accepted presentation, titled &ldquo;Auxiliary Diagnosis of COPD With Cough Search and Portable Spirometry: A Multicenter, Prospective, Comparative Validation Study,&rdquo; will be featured at ATS 2026, one of the world&rsquo;s most influential scientific gatherings for pulmonology, critical care, and respiratory innovation.'),
    H('Driving Global Adoption of Sound- and Movement-Based Biomarkers'),
    P('Respiratory diseases remain one of the most pressing global health challenges, with COPD alone responsible for millions of deaths annually and billions in economic burden. Traditional diagnostic pathways remain costly, infrastructure-dependent, and inaccessible for large segments of the global population.'),
    P('Luca Healthcare&rsquo;s sound-based biomarker platform is increasingly being adopted by pharmaceutical partners seeking scalable digital endpoints, remote patient monitoring, and predictive algorithms that enhance clinical trial efficiency and support earlier, more personalized intervention. Luca is also advancing movement-based digital biomarkers, enabling objective, sensor-driven assessment of gait, tremor, and motor function to further expand its portfolio of clinically meaningful endpoints. These multimodal algorithms are being integrated directly into May, Luca&rsquo;s AI health agent, enabling real-time, software-based screening and monitoring that can be deployed globally at population scale.'),
    P('By enabling continuous assessment using widely accessible data such as cough acoustics and movement signals, Luca&rsquo;s technology offers a cost-effective path to global screening and disease management&mdash;including in low-resource settings where traditional diagnostics remain inaccessible.'),
    H('A Strengthening Global Trajectory'),
    Q('&ldquo;Being selected to present at ATS 2026 is another strong validation of our scientific rigor and the global relevance of our work. We are continuing the momentum from ERS and gaining meaningful traction worldwide as sound- and movement-based biomarkers emerge as powerful tools for drug research, clinical development, and AI-enabled healthcare delivery.&rdquo;', 'Echo Chen, PhD, CEO of Luca Healthcare'),
  ],
))

articles.append(dict(
  slug='coughsearch-ant-group-bund-2025', tag='Partnership',
  title='Luca&rsquo;s CoughSearch&reg; Debuts on Ant Group&rsquo;s AQ Platform at Bund 2025 — Redefining Respiratory Diagnostics with AI',
  date='Shanghai, China — September 13, 2025',
  desc='Luca Healthcare unveiled CoughSearch® at the Inclusion-Bund Conference hosted by Ant Group, as an ecosystem partner of Ant Health&rsquo;s AQ medical AI platform.',
  lead='Luca Healthcare unveiled its flagship respiratory diagnostic tool, CoughSearch&reg;, at the Inclusion-Bund Conference hosted by Ant Group&mdash;one of the world&rsquo;s most influential technology events highlighting cutting-edge digital innovations across AI and digital health.',
  blocks=[
    P('At the Future Health Pavilion, Luca unveiled its breakthrough product&mdash;CoughSearch&reg;, an AI-powered diagnostic tool that analyzes cough sounds to detect pulmonary diseases. As an ecosystem partner of Ant Health&rsquo;s AQ medical AI platform, CoughSearch&reg; drew significant attention from attendees, media, and healthcare experts.'),
    P('This year&rsquo;s conference, themed &ldquo;Inclusion,&rdquo; featured over 10,000 square meters of exhibition space, covering AGI, robotics, future health, and intelligent payments. The Future Health Pavilion showcased Ant Health&rsquo;s latest AI applications in disease screening, health management, and medical services through interactive experiences.'),
    P('The CoughSearch&reg; demo allowed users to generate a diagnostic report in under one minute using just 3&ndash;5 voluntary cough sounds. Over the four-day event, the technology became a standout attraction, with visitors lining up to assess their coughs. After receiving their diagnostic reports, users could engage with AQ for personalized interpretation and health guidance.'),
    Q('&ldquo;Cough sounds are bio-signatures that hold the potential to help solve a global respiratory crisis that impacts 750 million people with chronic respiratory diseases and over 1 billion new patients with acute infections annually.&rdquo;', 'Dr. Echo Chen, CEO of Luca Healthcare'),
    P('The integration of AQ&rsquo;s medical language model with Luca&rsquo;s digital biomarker technology is shaping the next generation of AI-powered healthcare. Looking ahead, users will be able to assess their respiratory health in real time via CoughSearch&reg;, and seamlessly access follow-up services such as symptom checking, report analysis, and online appointments, all powered by AQ. AI is no longer just a tool&mdash;it&rsquo;s becoming a 24/7 intelligent health companion.'),
    P('Luca Healthcare remains committed to advancing digital respiratory medicine. Through innovative, clinically-validated technologies and strategic partnerships, Luca continues to drive the real-world adoption of AI healthcare for all.'),
  ],
))

articles.append(dict(
  slug='santo-biotech-car-t', tag='Partnership',
  title='Luca Healthcare and SANTO Biotech Forge Strategic Alliance to Advance AI-Enabled Safety Intelligence in In Vivo CAR-T Therapies',
  date='Hangzhou, China — August 22, 2025',
  desc='Luca Healthcare and SANTO Biotech partner to co-develop AI-powered digital health technologies for cell and gene therapies, including CAR-T.',
  lead='Luca Healthcare and SANTO Biotech (Hangzhou) Co., Ltd. have entered into a strategic partnership to co-develop cutting-edge AI-powered digital health technologies (DHT) for clinical applications in cell and gene therapies, including CAR-T, TCR-T, gene therapy, and gene editing.',
  blocks=[
    P('This collaboration will focus on integrating remote monitoring and patient-centric data capture into clinical development workflows, while jointly building and validating AI capabilities for early detection of high-risk safety events&mdash;specifically Cytokine Release Syndrome (CRS) and Immune Effector Cell-Associated Neurotoxicity Syndrome (ICANS). The goal is to elevate patient safety, streamline trial operations, and enhance the quality of clinical evidence.'),
    P('SANTO Biotech is a trailblazer in in vivo gene therapy, leveraging proprietary next-generation lentiviral vector technologies. With over 20 years of expertise in vector engineering and disease mechanism research, the company has contributed extensively to top-tier scientific publications. Its three core platforms&mdash;the 5G Vector Delivery System, Animal Disease Modeling Platform, and Process Optimization Platform&mdash;form a robust, self-sustaining biotech ecosystem. SANTO is focused on developing transformative therapies for high-burden conditions such as neurofibromatosis, meningioma, and malignant mesothelioma, and is actively working to integrate gene therapies into national reimbursement frameworks.'),
    P('In vivo CAR-T therapy represents a rapidly advancing frontier in oncology and immunotherapy. Despite its therapeutic promise, it is frequently associated with serious adverse events&mdash;including CRS, ICANS, hematologic toxicities, and opportunistic infections&mdash;stemming from T-cell activation, cytokine surges, and immune system disruption. Early prediction, real-time monitoring, and precision intervention are essential to mitigating these risks and optimizing clinical outcomes.'),
    P('Through this alliance, Luca Healthcare and SANTO Biotech will harness AI to build predictive safety models and dynamic risk management tools for in vivo CAR-T therapies, aiming to redefine clinical control and maximize patient benefit.'),
    Q('&ldquo;AI and in vivo CAR-T are converging to shape the future of precision medicine. We&rsquo;re honored to partner with Luca Healthcare to deliver safer, smarter therapeutic solutions for cancer patients worldwide.&rdquo;', 'Dr. Lu Zhou, CEO of SANTO Biotech'),
    Q('&ldquo;We&rsquo;re excited to collaborate with SANTO Biotech on this transformative journey. CAR-T therapy is a cornerstone of next-generation oncology, and our vision for AI-powered digital biomarkers and disease management is deeply aligned. Together, we aim to accelerate innovation and unlock new hope for patients.&rdquo;', 'Dr. Echo Chen, CEO of Luca Healthcare'),
  ],
))

articles.append(dict(
  slug='ametris-actigraph-partnership', tag='Partnership',
  title='Ametris (formerly ActiGraph) and Luca Healthcare Announce Strategic Partnership to Accelerate Digital Health Solutions in Clinical Trials Across US and China',
  date='Pensacola, FL, USA & Shanghai, China — August 25, 2025',
  desc='Ametris and Luca Healthcare announce a strategic partnership to enhance the adoption of Digital Health Tools in clinical trials across the US and China.',
  lead='Ametris, a global digital health solutions provider transforming real-world patient data into validated clinical evidence, and Luca Healthcare, a leader in using AI and machine learning to develop predictive healthcare solutions, today announced a strategic partnership aimed at significantly enhancing the adoption and deployment of Digital Health Tools (DHTs) in clinical trials, particularly within the rapidly evolving US and Chinese markets.',
  blocks=[
    P('This collaboration comes at a pivotal time, as clinical trial trends in both the US and China show a strong inclination towards digital transformation, driven by the need for greater efficiency, patient centricity, and real-world data collection. The integration of advanced digital health technologies is proving crucial in streamlining drug development, reducing costs, and ultimately bringing life-changing therapies to patients faster.'),
    Q('&ldquo;We are incredibly excited to partner with Luca Healthcare to expand the reach and impact of our digital health solutions. By combining Ametris&rsquo;s expertise in validated real-world data collection with Luca&rsquo;s innovative AI-driven solutions and strong presence in the Chinese and Asian markets, we are poised to accelerate drug development for pharmaceutical companies in both the US and China, ultimately benefiting patients worldwide.&rdquo;', 'Jeremy Wyatt, CEO of Ametris'),
    P('Under this strategic partnership, Luca Healthcare will help expand Ametris&rsquo;s existing business in China and Asia by integrating Ametris&rsquo;s wearable technologies to pharmaceutical partners, enabling Ametris to offer a full range of Decentralized Clinical Trial (DCT) products and services for the Chinese and Asian markets. Concurrently, Ametris will support Luca&rsquo;s business expansion in the US, enabling Luca to offer clinically validated AI solutions in both clinical trials and as digital companions.'),
    Q('&ldquo;Our mission at Luca Healthcare is to provide affordable, accessible, and clinically validated digital health solutions. This partnership with Ametris is a significant step forward in achieving that mission on a global scale. By integrating Ametris&rsquo;s robust digital health tools with our AI-driven predictive capabilities, we can offer a comprehensive suite of solutions that will accelerate clinical trials in both the US and China.&rdquo;', 'Echo Chen, PhD, CEO of Luca Healthcare'),
    H('About Ametris'),
    P('Ametris (formerly ActiGraph) is a global digital health solutions provider transforming real-world patient data into validated clinical evidence. Ametris&rsquo;s technologies are utilized by pharmaceutical, biotechnology, and academic researchers worldwide to objectively measure and analyze patient activity, sleep, and other physiological parameters in clinical trials and research studies.'),
  ],
))

articles.append(dict(
  slug='dime-adrd-alliance', tag='Alliance',
  title='Luca Healthcare Joins Global Alliance Initiated by DiMe to Build Digital Measures for Alzheimer&rsquo;s Disease and Related Dementias',
  date='Shanghai — August 16, 2023',
  desc='Luca Healthcare joins a DiMe-initiated global alliance to define core digital clinical measures for Alzheimer&rsquo;s disease and related dementias.',
  lead='Luca Healthcare today announced it has entered into a partnership initiated by the Digital Medicine Society (DiMe) to define a set of core digital clinical measures for Alzheimer&rsquo;s disease and related dementias (ADRD), alongside the Alzheimer&rsquo;s Drug Discovery Foundation, Biogen, Boston University, Eisai, Eli Lilly and Company, and Merck.',
  blocks=[
    P('By working together with a balanced and inclusive group of global multistakeholder experts&mdash;including pharmaceutical companies, patients, care partners, clinicians, clinical scientists, technological, regulatory, and payer experts&mdash;there is an opportunity to define meaningful global aspects of health and build consensus for a set of core digital clinical measures in ADRD at the intersection of technological capabilities. Luca will drive the effort to guide and coordinate participant clinicians, care partners and patients from China.'),
    P('Globally, ADRD affects 47 million people and the expected growth is staggering, with cases expected to double every 20 years. The collaboration aims to tackle one of the greatest challenges in advancing therapies for ADRD: a lack of measures that can actually determine whether new potential treatments are working. By defining an optimized set of core digital clinical measures that address patient, care partner, and clinical unmet needs, this project aims to transform ADRD research and care.'),
    P('Increasingly, digital tools such as wearable sensors are being used to provide complete and precise information about the impact of disease on patients&rsquo; lives. These technologies and the data they generate help quantify the disease in a patient-centered way, resulting in digital indicators that can be used to speed the successful development of effective new treatments and better manage disease during routine care.'),
    Q('&ldquo;Digital measures offer enormous promise to bolster collective understanding of Alzheimer&rsquo;s disease and related dementias. These measures can deepen our knowledge of disease progression, define new disease phenotypes, and support earlier diagnosis&mdash;all critically important insights for a condition where inaccurate and delayed diagnosis is common.&rdquo;', 'Dr. Jian Yang, Associate Vice President of Digital Health, Eli Lilly and Company'),
    Q('&ldquo;China has over 265 million people aged 60 years and above, of which 40 million people have mild cognitive impairment with 15 million people having a form of dementia. With ADRD, early diagnosis is key. We are pleased to join this global initiative and contribute to help better understand and treat this disease.&rdquo;', 'Dr. Echo Chen, CEO of Luca Healthcare'),
    Q('&ldquo;Rapid advances in digital technologies present unparalleled opportunities to transform the way neurodegenerative diseases can be predicted, diagnosed, prevented and treated. We are delighted to be partnering with leading organizations like Luca Healthcare&mdash;their expertise in digital biomarkers and digital health solution development will have a significant impact on our collective work to establish core digital clinical measures for ADRD.&rdquo;', 'Jennifer Goldsack, CEO of DiMe'),
  ],
))

articles.append(dict(
  slug='pwc-strategy-partnership', tag='Partnership',
  title='PwC (China) and Luca Healthcare Announce a Strategic Partnership to Build Digital Health Solutions for Life Sciences Companies',
  date='Shanghai — February 17, 2023',
  desc='Strategy&, the strategy consulting team at PwC, and Luca Healthcare announce a strategic partnership to build digital health solutions for life sciences companies.',
  lead='Strategy&, the strategy consulting team at PwC, and Luca Healthcare today announced a strategic partnership to accelerate collaboration to build digital health solutions for life sciences companies.',
  blocks=[
    P('Dr. Echo Chen, CEO of Luca Healthcare, and Mr. William Zhang, partner at Strategy& and head of China healthcare and life sciences for PwC&rsquo;s strategy consulting group, together attended the signing ceremony. The collaboration will integrate each company&rsquo;s core offerings and leverage each other&rsquo;s resources to empower life sciences companies with innovative digital health solutions that let patients take greater control of their health.'),
    Q('&ldquo;Digital health solutions centered around digital biomarkers and AI can help predict, prevent, diagnose and treat diseases in a much more accessible way and deliver better clinical outcomes for patients. Combining PwC&rsquo;s advantages in client resources and industry insights, and Luca Healthcare&rsquo;s medical and AI expertise, the two companies can cover a wide spectrum of digital health strategies and solutions.&rdquo;', 'Dr. Echo Chen, CEO of Luca Healthcare'),
    Q('&ldquo;Digital health tools will drastically improve health quality over the coming years by helping to bridge care gaps, expand access, enable more personalized treatment, and eliminate geographic barriers. We hope to join with Luca to help all participants in the industry and create a new ecosystem for digital health with industry-leading technologies and business consulting capabilities.&rdquo;', 'William Zhang, Partner at Strategy& / PwC'),
    P('The partnership between PwC and Luca Healthcare represents a significant step in advancing the digital healthcare industry in China and beyond. With PwC&rsquo;s global experience and expertise and Luca Healthcare&rsquo;s innovative solutions, the two companies are well-positioned to create new and exciting opportunities for patients and healthcare providers alike.'),
  ],
))

articles.append(dict(
  slug='cambridge-cognition-partnership', tag='Partnership',
  title='Cambridge Cognition and Luca Healthcare Announce a Strategic Partnership and Exclusive Licensing Agreement for the China Market',
  date='Shanghai — November 28, 2022',
  desc='Cambridge Cognition and Luca Healthcare announce a 10-year exclusive licensing agreement to commercialize cognitive assessment tools, including CANTAB™, in China.',
  lead='Cambridge Cognition, a leading technology company that develops digital solutions to assess brain health, and Luca Healthcare, China&rsquo;s category leader in clinically validated digital health solutions, today announced a strategic partnership and a 10-year exclusive licensing agreement to commercialize Cambridge Cognition&rsquo;s suite of cognitive assessment tools in the China market.',
  blocks=[
    P('Generally considered the gold standard in cognitive assessment tools, Cambridge Cognition&rsquo;s technologies have been used in over 2,500 studies, in more than 100 countries and 50 languages, to assess over 1 million patients. The company remains at the forefront of research in the field, investing millions of pounds each year in cutting-edge new developments.'),
    Q('&ldquo;We are delighted to enter this partnership with Luca Healthcare to deploy Cambridge Cognition&rsquo;s products in China. For over 30 years, our technology has been at the forefront of scientific discovery, delivering value to research institutions, healthcare providers and pharmaceutical and biotechnology companies worldwide, and we plan to work closely with Luca Healthcare to make these solutions available in clinical trials and for patients across China.&rdquo;', 'Matthew Stork, CEO of Cambridge Cognition'),
    P('A key component of this partnership brings the CANTAB&trade; suite of tools to the China commercial market. Originally developed at the University of Cambridge, CANTAB&trade; includes highly sensitive, precise, and objective measures of cognitive function&mdash;demonstrating sensitivity to changes across working memory, learning, executive function, and visual, verbal, and episodic memory. The assessments are language-independent and the instructions are already available in Chinese.'),
    P('Luca plans to make these tools available to the China market through the LucaPlex&reg; platform that serves their pharmaceutical and commercial partners in China. Cambridge Cognition&rsquo;s assessments are hosted in a secure cloud-based server in China and can be run seamlessly within LucaPlex&reg; using APIs.'),
    Q('&ldquo;China has over 265 million people aged 60 years and above, of which 40 million people have mild cognitive impairment with 15 million people having a form of dementia. With neurodegenerative diseases, early diagnosis is the key to managing disease progression. Luca&rsquo;s mission is to make healthcare more affordable and more accessible; this partnership certainly gives us an opportunity to do that for those impacted by neurodegenerative disorders in China.&rdquo;', 'Echo Chen, PhD, CEO of Luca Healthcare'),
  ],
))

articles.append(dict(
  slug='thermo-fisher-collaboration', tag='Partnership',
  title='Thermo Fisher Scientific (China) and Luca Healthcare Announce a Strategic Collaboration to Support Direct-to-Patient Clinical Trial Services in China',
  date='Shanghai — November 6, 2021',
  desc='Thermo Fisher Scientific (China) and Luca Healthcare announce a collaboration to develop a digital patient assistant and medication adherence solutions for DTP clinical trials.',
  lead='Thermo Fisher Scientific (China), the world leader in serving science, and Luca Healthcare, China&rsquo;s category leader in clinically validated, software-based screening, treatment and patient management tools, today at the 4th China International Import Expo (CIIE) announced a strategic collaboration to explore developing a digital patient assistant data platform and digital medication adherence solutions to support direct-to-patient clinical trial services in China.',
  blocks=[
    Q('&ldquo;We look forward to working with Luca Healthcare to add digital solutions to our clinical service offerings, particularly as we continue to enhance our capabilities to support a more patient-centric model for clinical trial services.&rdquo;', 'Hann Pang, President of Thermo Fisher Scientific China'),
    Q('&ldquo;We are excited to partner with Thermo Fisher Scientific to integrate with existing DTP drug home delivery services, mobile nurse, and at-home patient data collection capabilities through a single digital patient assistant, and provide study sponsors with visibility, communication, and full access to trial patients. With the rapid emergence of decentralized clinical trials, we look forward to working with clinical trial services providers and CROs to facilitate both virtual and hybrid clinical trials.&rdquo;', 'Echo Chen, PhD, CEO of Luca Healthcare'),
    H('About Thermo Fisher Scientific (China)'),
    P('Thermo Fisher Scientific (China) Co., Ltd has been operating in China for over 35 years. Headquartered in Shanghai, it has branch offices across the country with around 5,000 employees, providing comprehensive laboratory solutions and serving customers across various industries. The company is committed to enabling its customers to make the world healthier, cleaner and safer.'),
  ],
))

articles.append(dict(
  slug='astrazeneca-respiratory-partnership', tag='Partnership',
  title='AstraZeneca (China) and Luca Healthcare Announce a Strategic Partnership for Out-of-Hospital Digital Tools for Respiratory Diseases',
  date='Shanghai — November 5, 2021',
  desc='AstraZeneca (China) and Luca Healthcare announce a strategic partnership to develop out-of-hospital digital tools for screening and management of respiratory diseases.',
  lead='AstraZeneca (China), a global innovation-led biopharmaceutical company, and Luca Healthcare, China&rsquo;s category leader in clinically validated, software-based screening, treatment and patient management tools, today during the opening of the 4th China International Import Expo (CIIE) announced a strategic partnership to develop out-of-hospital digital tools for screening and management of respiratory diseases and to explore digital solutions to support R&D and clinical trials in China.',
  blocks=[
    P('Despite being a common, preventable, and treatable disease, chronic obstructive pulmonary disease (COPD) is the fifth leading cause of death in China. The reported prevalence of COPD is 8.2% for those over the age of 40, or approximately 100 million people. In addition, there are another 45 million asthma patients in China. Current diagnosis rates are 30% and 28% for COPD and asthma, respectively&mdash;many remain undiagnosed, and raising awareness is the first step to improving rates of diagnosis.'),
    Q('&ldquo;We look forward to working with AstraZeneca and China&rsquo;s leading respiratory experts on developing algorithms to screen for respiratory diseases and manage exacerbations. More importantly, our digital tools will be developed and clinically tested specifically for Chinese patients. With the emergence of internet hospitals, third-party telemedicine platforms and other digital health channels, there are 620 million consumers in China who have touched an aspect of digital health. Luca Healthcare&rsquo;s clinically validated, out-of-hospital tools can provide objective, smartphone-based solutions to screen and manage a wide range of diseases in a non-clinical setting.&rdquo;', 'Echo Chen, PhD, CEO of Luca Healthcare'),
    H('About AstraZeneca'),
    P('AstraZeneca (LSE/STO/Nasdaq: AZN) is a global, science-led biopharmaceutical company that focuses on the discovery, development, and commercialization of prescription medicines in Oncology, Rare Diseases, and BioPharmaceuticals, including Cardiovascular, Renal & Metabolism, and Respiratory & Immunology. Based in Cambridge, UK, AstraZeneca operates in over 100 countries and its innovative medicines are used by millions of patients worldwide.'),
  ],
))

articles.append(dict(
  slug='shanghai-pharma-home-delivery', tag='Partnership',
  title='Shanghai Pharmaceuticals and Luca Healthcare Announce a Strategic Collaboration to Provide Home Drug Delivery to Rare Disease Patients',
  date='Shanghai — October 12, 2021',
  desc='SPH Health Commerce and Luca Healthcare partner to provide online medication refills and home delivery to rare disease patients on Luca&rsquo;s patient management platform.',
  lead='SPH Health Commerce, the Direct-to-Patient (DTP) retail pharmacy subsidiary of Shanghai Pharmaceuticals, and Luca Healthcare, China&rsquo;s category leader in clinically validated, software-based screening, treatment and management tools, today announced a strategic partnership to provide Luca&rsquo;s patient management platform with online medication refills and delivery capabilities.',
  blocks=[
    P('The collaboration connects Luca&rsquo;s platform to SPH&rsquo;s internet hospital, 24&times;7 pharmacist call center, and a network of approximately 100 DTP retail pharmacies covering all major first- and second-tier cities.'),
    Q('&ldquo;We are delighted to enter into this strategic alliance with Luca Healthcare to provide online physician support and direct access to medication for patients with chronic and rare diseases. Luca&rsquo;s home-based monitoring tools allow physicians to make assessments based on more objective insights and measures. The integration of our internet hospital and drug home delivery ecosystem will bring great convenience and significant value to patients.&rdquo;', 'Gong Xiao Dong, Vice President of SPH Health Commerce'),
    Q('&ldquo;China&rsquo;s 20 million rare disease patients have limited options to manage their diseases. Our patient-centric mini-programs and apps supported by disease-specific patient groups consistently reach over 80% patient stickiness and significantly improved patients&rsquo; quality of life. Adding Shanghai Pharma&rsquo;s internet hospital platform and a national home drug delivery network will greatly enhance this experience.&rdquo;', 'Echo Chen, PhD, CEO of Luca Healthcare'),
  ],
))

for a in articles:
    build(**a)
print('TOTAL:', len(articles))
