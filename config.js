// Girl Gone AI — site config.
// Toggle features here. Values surface to client-side JS via window.NOVOCLAW_CONFIG.
window.NOVOCLAW_CONFIG = {
  // --- Storefront ---
  storefront: "stripe",
  storefrontName: "Stripe",
  stripeEnabled: true,
  apiUrl: "/api",
  subscriberCount: 200,
  formspreeFormId: "",
  formsubmitEmail: "kenny@novolinkai.com",
  demoMode: false,

  // --- Social sign-in (paste IDs here once registered) ---
  // Google: create OAuth Client ID at https://console.cloud.google.com → APIs & Services → Credentials.
  //         Authorized JS origin: https://girlgone.ai
  //         Authorized redirect URI: https://girlgone.ai/login.html
  googleClientId: "",
  // Apple: requires Apple Developer account ($99/yr). Create a Services ID at
  //        https://developer.apple.com/account/resources/identifiers — use the Services ID here.
  //        Configured Return URL: https://girlgone.ai/login.html
  appleClientId: "",

  // --- Ad conversion labels (Google Ads → Goals → Conversions) ---
  // Purchase label is already live; add the other two once created in Google Ads.
  googleAdsId: "AW-18123569132",
  googleAdsPurchaseLabel: "gKkPCPid26McEOzv_sFD",
  googleAdsLeadLabel: "",          // email signup / newsletter / waitlist
  googleAdsInitiateCheckoutLabel: "", // clicked "Buy Now" on a product

  // --- Meta Pixel (already wired in HTML) ---
  metaPixelId: "960211666721135"
};
