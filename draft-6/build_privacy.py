# -*- coding: utf-8 -*-
"""Generate privacy-policy.html at draft-6 root, reusing contact.html header/footer."""
HEADER = open('/tmp/sprite_header_root.html').read()
FOOTER = open('/tmp/footer_root.html').read()

def H(t): return f'      <h2 class="art-h">{t}</h2>'
def P(t): return f'      <p>{t}</p>'
def UL(items):
    lis=''.join(f'<li>{i}</li>' for i in items)
    return f'      <ul class="art-list">{lis}</ul>'

blocks = []
blocks.append(P('This Site is owned and operated by Luca Healthcare (Shanghai) Co., Ltd. or one or more of its affiliates (collectively referred to as &ldquo;Luca Healthcare,&rdquo; &ldquo;us,&rdquo; &ldquo;we&rdquo; or &ldquo;our&rdquo;). This Policy applies when you use our website or certain other affiliated websites (Sites) that link to or post this Privacy Policy.'))
blocks.append(P('Certain uses or disclosures of personal information may be governed by other privacy notices. At times we may collect personal information about you that constitutes Protected Personal Information (PPI) pursuant to the Personal Information Protection Law of the People&rsquo;s Republic of China. Our use and disclosure of PPI is subject to our, or our customer&rsquo;s as applicable, User Privacy Policy of the specific products and not this Privacy Policy.'))
blocks.append(P('By visiting our Luca Healthcare Sites you consent to the collection, use and transfer of your personal data in accordance with this Privacy Policy.'))

blocks.append(H('1. What information do we collect about you?'))
blocks.append(P('In this Privacy Policy, &ldquo;personal data&rdquo; means information that may identify you as an individual directly or indirectly. Personal data does not include information that has been &ldquo;de-identified&rdquo; in such a way that your identity cannot reasonably be determined.'))
blocks.append(P('If you visit our Sites, we may collect information that personally identifies you, including your name, telephone number, and email address (&ldquo;personal data&rdquo;) from you, only if you provide us with such information.'))
blocks.append(P('We will indicate if the collection and provision of certain categories of personal data is mandatory. For any such categories, we may not be able to provide you with the services on our Sites if you do not provide us with the required information.'))
blocks.append(P('<strong>When you visit our Sites.</strong> Luca Healthcare collects industry-standard data from everyone who visits our Sites &mdash; even if you don&rsquo;t have a Luca Healthcare account. This includes log data that automatically records information about your visit, such as your browser type, operating system, the URL of the page that referred you, the different actions you performed, and the IP address you used to access pages on the Sites. We use this type of information to provide you with an experience that&rsquo;s relevant to your location based on the IP address, to prevent Sites misuse, and to ensure the Sites are working properly. We also collect data from cookies (see our Cookie Policy below).'))
blocks.append(P('<strong>When you contact us.</strong> Whenever you contact Luca Healthcare using the &ldquo;Contact Us&rdquo; form, we collect your name, email address, company name, job title and geographic region, along with additional information you provide in your request so that we can provide you with the requested assistance.'))

blocks.append(H('2. How we use your personal data'))
blocks.append(P('You consent to Luca Healthcare collecting, using and disclosing your personal data for the following purposes:'))
blocks.append(UL([
  'responding to, handling, and processing your queries, requests, applications, complaints, and feedback;',
  'subject to your consent, sending you notifications and informing you about new features, products or services we think you would be interested in. You may withdraw your consent by contacting us at the email address provided below or follow the steps to unsubscribe presented in communications you receive from us;',
  'using data and logs in research to understand and improve the Luca Healthcare Sites; to troubleshoot the Sites; to detect and protect against error, fraud or other criminal activity; and to protect the security or integrity of the Sites;',
  'disclosing or transferring your personal data to other entities within the Luca Healthcare group of companies to allow them to provide you with the services that you have requested;',
  'complying with any applicable laws, regulations, codes of practice, guidelines, or rules, or to assist in law enforcement and investigations conducted by any governmental and/or regulatory authority; and',
  'any other incidental business purposes related to or in connection with the above.',
]))
blocks.append(P('In the event of a corporate sale, merger, reorganization, dissolution or similar event, your personal data may be part of the assets that is transferred (&ldquo;business asset transaction&rdquo;). You consent to such transfer and acknowledge that any successor or acquirer of Luca Healthcare or its assets will continue to have the right to use your personal data in accordance with the terms of this Privacy Policy.'))

blocks.append(H('3. Retention of your personal data'))
blocks.append(P('We will only retain your personal data until it is reasonable to assume that such retention no longer serves the purpose for which your personal data was collected and is no longer necessary for legal or business purposes.'))

blocks.append(H('4. Access to your personal data'))
blocks.append(P('We will use all reasonable endeavors to keep your personal data accurate, complete, up-to-date, relevant and not misleading. Please contact us at <a href="mailto:contactus@lucahealthcare.com">contactus@lucahealthcare.com</a> if you would like to access the personal data that we hold about you, correct any personal data that is inaccurate, incomplete or out-of-date, withdraw your consent to the collection, use and disclosure of your personal data, or request that your personal data be deleted. We will use reasonable endeavors to provide a complete list of your personal data, or correct or delete your personal data, within a reasonable period of receipt of your request.'))
blocks.append(P('If you would like to request that we delete all personal data, please contact us at <a href="mailto:contactus@lucahealthcare.com">contactus@lucahealthcare.com</a>. Our ability to comply with your deletion request is subject to any applicable legal or other requirement to maintain certain records. Please note that the deletion of your personal data from our database may result in us not being able to provide you with some services on our Sites.'))

blocks.append(H('5. Luca Healthcare&rsquo;s policies for children'))
blocks.append(P('This Site is not directed at persons under the age of 14. We do not knowingly collect any personal data from children under 14. If you are under the age of 18, you may only use the Site with the consent of and under the supervision of your parent or legal guardian, who shall be responsible for all your activities.'))

blocks.append(H('6. Storage and security of your personal data'))
blocks.append(P('We will use all reasonable endeavors to maintain the security of your personal data and to protect it from misuse, interference and loss and against unauthorized collection, copying, access, modification or disclosure. We will destroy or anonymize any personal data we hold about you which is no longer required under the terms of this Privacy Policy.'))
blocks.append(P('Due to the nature of the internet, we do not provide any guarantee or warranty regarding the security of your personal data during transmission to or storage by us, and you acknowledge that you disclose your personal data to us at your own risk. Please contact us immediately if you become aware or have reason to believe there has been any unauthorized use of your personal data in connection with the Luca Healthcare Sites.'))

blocks.append(H('7. Cookie Policy'))
blocks.append(P('Some of the information that we collect will not personally identify you but will instead track your use of the Sites so that we can better understand how the Sites are used and in turn enhance and improve your experience. This information can be obtained through the use of cookies. Cookies are a small data file transferred to your device that recognizes and identifies your device and allows it to &lsquo;remember&rsquo; information from the Sites for future use. We may collect technical information from your web browser or mobile device, for example, location data and certain characteristics of, and performance data about, your device, carrier/operating system including device and connection type and IP address. Unless you have elected to remain anonymous through your device and/or web browser, the above-mentioned information may be collected and used by us automatically through your use of the Sites.'))
blocks.append(P('You have a number of options to control or limit how we and our partners use cookies and similar technologies, including for advertising. Although most browsers and devices accept cookies by default, their settings usually allow you to clear or decline cookies. If you disable cookies, however, some of the features of the Sites may not function properly.'))
blocks.append(P('Check your mobile device for settings that control ads based on your interactions with the applications on your device. For example, on your iOS device, enable the &ldquo;Limit Ad Tracking&rdquo; setting, and on your Android device, enable the &ldquo;Opt out of Ads Personalization&rdquo; setting.'))
blocks.append(P('The Sites do not respond to Do Not Track signals because we do not track our users over time and across third-party websites to provide targeted advertising. However, we believe that you should have a choice regarding interest-based ads served by our partners, which is why we outline the options available to you above.'))

blocks.append(H('8. Changes to our Privacy Policy'))
blocks.append(P('Luca Healthcare reserves the right to amend all or any part of this Privacy Policy. Any changes will be notified through the Sites and/or, where appropriate, through email notification. Your continued use of the Sites after any such changes are notified to you constitutes your agreement to this Privacy Policy as amended.'))

blocks.append(H('9. Links to other websites and applications'))
blocks.append(P('The Sites may have links to other websites or applications. We are not responsible for the security or privacy of any information collected by such websites and, while we do not permit those websites to track your use of the Luca Healthcare Sites, we are unable to control whether such tracking mechanisms are implemented by those apps or websites. You should exercise caution and review the privacy statements applicable to the third-party websites and services you use.'))

blocks.append(H('10. Effect of Privacy Policy'))
blocks.append(P('This Privacy Policy applies in conjunction with any other policies, notices, contractual clauses and consent statements that apply in relation to the collection, use and disclosure of your personal data by us.'))

blocks.append(H('11. Contact us'))
blocks.append(P('All comments, queries and requests relating to our use of your personal data are welcomed and should be addressed to our data protection officer at <a href="mailto:contactus@lucahealthcare.com">contactus@lucahealthcare.com</a>.'))
blocks.append(P('If you have questions or complaints in relation to the use of your personal data, or would like to request to access, update, or delete it, you may also contact our data protection officer at <a href="mailto:contactus@lucahealthcare.com">contactus@lucahealthcare.com</a>.'))

body = '\n'.join(blocks)

PAGE = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Privacy Policy — Luca Healthcare</title>
  <meta name="description" content="Luca Healthcare Privacy Policy — how we collect, use, store and protect your personal data." />
  <link rel="icon" href="assets/img/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="assets/img/favicon-180.png" />
  <meta name="theme-color" content="#009EDF" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/css/main.css?v=14" />
</head>
<body>

{HEADER}

<main>
  <article class="article">
    <div class="container art-container">
      <a href="index.html" class="art-back"><svg viewBox="0 0 24 24" style="transform:rotate(180deg)"><use href="#i-arrow"/></svg> Back home</a>
      <span class="art-tag">Legal</span>
      <h1 class="art-title">Privacy Policy</h1>
      <div class="art-meta">Effective 28 September 2023</div>
      <div class="art-lead">Luca Healthcare knows that you care about how information about you is used and shared. This Policy explains what we may do with information that we collect from or about you when you use our Sites.</div>
      <div class="art-body">
{body}
      </div>
    </div>
  </article>
</main>

{FOOTER}

<script src="assets/js/i18n-dict.js?v=11"></script>
<script src="assets/js/main.js?v=4"></script>
</body>
</html>
'''
open('privacy-policy.html','w').write(PAGE)
print('wrote privacy-policy.html', len(PAGE), 'chars')
