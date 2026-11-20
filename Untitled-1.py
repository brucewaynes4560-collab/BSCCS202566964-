:root {
  font-family: "Aptos", "Segoe UI", Arial, sans-serif;
  --ink: #07111b;
  --lime: #b7f36a;
  --green: #16835d;
  --amber: #b65f12;
  --red: #bd3b3b;
}

* { box-sizing: border-box; }
html { -webkit-font-smoothing: antialiased; }
body { margin: 0; }
button, input, textarea { font: inherit; }
button { cursor: pointer; }
a { color: inherit; }
::selection { background: var(--lime); color: var(--ink); }
:focus-visible { outline: 3px solid #66834b; outline-offset: 4px; }

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  font-size: 18px;
  font-weight: 900;
  letter-spacing: -.04em;
}

.mark {
  display: grid;
  place-items: center;
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: var(--lime);
  color: var(--ink);
  font-size: 24px;
  flex-shrink: 0;
}

body.auth-page {
  color-scheme: dark;
  background: var(--ink);
  color: #eef6f3;
  --muted: #aebdbb;
}

.auth-page .grid {
  min-height: 100vh;
  background-image:
    linear-gradient(rgba(255,255,255,.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.035) 1px, transparent 1px);
  background-size: 72px 72px;
  background-position: center top;
  overflow: hidden;
}

.auth-page .top,
.auth-page .stage {
  width: min(100% - 40px, 1400px);
  margin-inline: auto;
}

.auth-page .top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-block: 24px;
  gap: 20px;
}

.auth-page .mark {
  box-shadow: 0 0 0 5px rgba(183,243,106,.08);
}

.auth-page .motto {
  border: 1px solid rgba(255,255,255,.1);
  background: rgba(255,255,255,.04);
  border-radius: 999px;
  padding: 9px 16px;
  color: rgba(255,255,255,.7);
  font-size: 14px;
}

.auth-page .stage {
  display: grid;
  gap: 64px;
  padding-block: 56px 96px;
  align-items: center;
}

.auth-page .eyebrow {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 30px;
  color: var(--lime);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .2em;
  text-transform: uppercase;
}

.auth-page .eyebrow::before {
  content: "";
  width: 40px;
  height: 1px;
  background: var(--lime);
}

.auth-page h1 {
  max-width: 11ch;
  margin: 0;
  font-size: clamp(56px, 8vw, 124px);
  line-height: .9;
  letter-spacing: -.075em;
}

.auth-page .intro {
  max-width: 56ch;
  margin: 32px 0 0;
  color: var(--muted);
  font-size: 20px;
  line-height: 1.6;
}

.auth-page .steps {
  display: grid;
  gap: 12px;
  margin-top: 40px;
}

.auth-page .step {
  border-top: 1px solid rgba(255,255,255,.15);
  padding-top: 14px;
}

.auth-page .step b {
  display: block;
  color: var(--lime);
  font-size: 12px;
}

.auth-page .step span {
  display: block;
  margin-top: 8px;
  font-size: 14px;
  font-weight: 700;
  color: rgba(255,255,255,.85);
}

.auth-page .login-wrap {
  position: relative;
  width: 100%;
  max-width: 560px;
  margin-inline: auto;
}

.auth-page .corner {
  position: absolute;
  width: 96px;
  height: 96px;
  pointer-events: none;
}

.auth-page .corner.a {
  left: -20px;
  top: -20px;
  border-left: 1px solid rgba(183,243,106,.45);
  border-top: 1px solid rgba(183,243,106,.45);
}

.auth-page .corner.b {
  right: -20px;
  bottom: 4px;
  border-right: 1px solid rgba(183,243,106,.45);
  border-bottom: 1px solid rgba(183,243,106,.45);
}

.auth-page .card {
  position: relative;
  border: 1px solid rgba(255,255,255,.12);
  background: #0d1b27;
  padding: clamp(24px, 4vw, 38px);
  box-shadow: 0 28px 90px rgba(0,0,0,.34);
}

.auth-page .card-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 30px;
  gap: 20px;
}

.auth-page .kicker {
  margin: 0;
  color: #a1b3af;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .18em;
  text-transform: uppercase;
}

.auth-page .card h2 {
  margin: 8px 0 0;
  font-size: 26px;
  letter-spacing: -.04em;
}

.auth-page .lock { color: var(--lime); }

.auth-page .button {
  display: flex;
  width: 100%;
  min-height: 52px;
  align-items: center;
  justify-content: center;
  gap: 10px;
  border: 1px solid var(--lime);
  background: var(--lime);
  color: var(--ink);
  font: 800 16px/1.4 "Segoe UI", Arial, sans-serif;
  text-decoration: none;
  cursor: pointer;
}

.auth-page .button:hover { background: #cdf98f; }

.auth-page .fine {
  margin: 18px 0 0;
  text-align: center;
  color: #a1b3af;
  font-size: 14px;
  line-height: 1.65;
}

.auth-page .disclaimer {
  text-align: center;
  color: #9baaa6;
  font-size: 12px;
  line-height: 1.55;
}

.auth-page .auth-field {
  display: block;
  margin: 0 0 18px;
  font-size: 14px;
  font-weight: 700;
}

.auth-page .auth-input {
  display: block;
  width: 100%;
  height: 48px;
  margin-top: 8px;
  border: 1px solid #526269;
  background: #07111b;
  padding: 0 12px;
  color: #eef6f3;
  font: inherit;
  font-size: 16px;
  outline: none;
}

.auth-page .auth-input:focus {
  border-color: var(--lime);
  box-shadow: 0 0 0 3px rgba(183,243,106,.14);
}

.auth-page .auth-error {
  border: 1px solid #de8f79;
  background: #3a2425;
  color: #ffd6c8;
  padding: 13px;
  line-height: 1.5;
  font-size: 14px;
  margin-bottom: 20px;
  overflow-wrap: anywhere;
}

.auth-page .auth-switch {
  display: block;
  text-align: center;
  margin-top: 22px;
  color: var(--lime);
  font-size: 14px;
}

.auth-page .password-note {
  color: #aebdbb;
  font-size: 13px;
  line-height: 1.5;
  margin: -8px 0 18px;
}

.auth-page :focus-visible { outline-color: var(--lime); }

body.dashboard-page {
  color-scheme: light;
  background: #f5f8f6;
  color: var(--ink);
  --muted: #5f706a;
  --line: #d8e0dd;
}

.dashboard-page .top {
  position: sticky;
  z-index: 5;
  top: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 74px;
  border-bottom: 1px solid rgba(255,255,255,.1);
  background: var(--ink);
  padding: 12px clamp(18px, 4vw, 56px);
  color: #eef6f3;
  gap: 16px;
}

.dashboard-page .mark {
  width: 38px;
  height: 38px;
  border-radius: 11px;
}

.dashboard-page .account {
  display: flex;
  align-items: center;
  gap: 12px;
}

.dashboard-page .account form { margin: 0; }

.dashboard-page .avatar {
  display: grid;
  width: 38px;
  height: 38px;
  place-items: center;
  border: 1px solid rgba(183,243,106,.35);
  border-radius: 50%;
  background: rgba(183,243,106,.08);
  color: var(--lime);
  font-weight: 900;
  flex-shrink: 0;
}

.dashboard-page .identity { display: none; }

.dashboard-page .identity b,
.dashboard-page .identity span {
  display: block;
  max-width: 240px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.dashboard-page .identity b { font-size: 14px; }

.dashboard-page .identity span {
  margin-top: 2px;
  color: #a5b5b1;
  font-size: 12px;
}

.dashboard-page .logout {
  min-height: 40px;
  border: 1px solid rgba(255,255,255,.25);
  background: transparent;
  padding: 9px 12px;
  color: white;
  font-size: 14px;
  font-weight: 700;
}

.dashboard-page .logout:hover {
  background: rgba(255,255,255,.08);
}

.dashboard-page .page {
  width: min(100% - 32px, 1460px);
  margin: 0 auto;
  padding: 32px 0 64px;
}

.dashboard-page .page-head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 24px;
}

.dashboard-page .eyebrow {
  margin: 0 0 8px;
  color: #53625e;
  font-size: 12px;
  font-weight: 900;
  letter-spacing: .16em;
  text-transform: uppercase;
}

.dashboard-page h1 {
  margin: 0;
  font-size: clamp(32px, 4vw, 52px);
  letter-spacing: -.055em;
  line-height: 1.1;
}

.dashboard-page .page-head p:last-child {
  max-width: 46ch;
  margin: 12px 0 0;
  color: var(--muted);
  font-size: 16px;
  line-height: 1.55;
}

.dashboard-page .security-note {
  display: none;
  align-items: center;
  gap: 8px;
  border: 1px solid #cbd7d2;
  background: white;
  padding: 10px 13px;
  color: #53625e;
  font-size: 13px;
  font-weight: 700;
}

.dashboard-page .security-note i {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--green);
}

.dashboard-page .workspace { display: grid; gap: 18px; }

.dashboard-page .panel {
  min-width: 0;
  border: 1px solid var(--line);
  background: white;
  box-shadow: 0 10px 35px rgba(17,41,35,.055);
}

.dashboard-page .panel-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--line);
  padding: 18px 20px;
  gap: 18px;
}

.dashboard-page .panel-head h2 {
  margin: 0;
  font-size: 17px;
  letter-spacing: -.02em;
}

.dashboard-page .panel-head span {
  color: var(--muted);
  font-size: 12px;
}

.dashboard-page .form { padding: 20px; }
.dashboard-page .field { margin-bottom: 18px; }

.dashboard-page .field-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 8px;
}

.dashboard-page .field label {
  font-size: 14px;
  font-weight: 800;
}

.dashboard-page .optional,
.dashboard-page .count {
  color: #657570;
  font-size: 12px;
  font-weight: 500;
}

.dashboard-page .input,
.dashboard-page .textarea {
  width: 100%;
  border: 1px solid #bdcbc5;
  border-radius: 0;
  background: white;
  color: var(--ink);
  outline: none;
  transition: border-color .16s, box-shadow .16s;
  font-size: 16px;
}

.dashboard-page .input {
  height: 46px;
  padding: 0 13px;
}

.dashboard-page .textarea {
  min-height: 210px;
  resize: vertical;
  padding: 12px 13px;
  line-height: 1.55;
}

.dashboard-page .input:focus,
.dashboard-page .textarea:focus {
  border-color: #66834b;
  box-shadow: 0 0 0 3px rgba(183,243,106,.35);
}

.dashboard-page .input::placeholder,
.dashboard-page .textarea::placeholder {
  color: #6a7e76;
}

.dashboard-page .actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding-top: 2px;
}

.dashboard-page .primary,
.dashboard-page .secondary,
.dashboard-page .text-button {
  min-height: 46px;
  border: 1px solid var(--ink);
  border-radius: 0;
  padding: 0 18px;
  font-weight: 800;
}

.dashboard-page .primary {
  display: flex;
  flex: 1;
  align-items: center;
  justify-content: center;
  gap: 9px;
  background: var(--ink);
  color: white;
}

.dashboard-page .primary:hover { background: #152b3c; }

.dashboard-page button:disabled {
  cursor: wait;
  opacity: .6;
}

.dashboard-page .secondary {
  background: white;
  color: var(--ink);
}

.dashboard-page .secondary:hover { background: #f0f4f2; }

.dashboard-page .text-button {
  border-color: transparent;
  background: transparent;
  color: #53655e;
}

.dashboard-page .text-button:hover { text-decoration: underline; }

.dashboard-page .form-note {
  display: flex;
  gap: 10px;
  margin: 18px 0 0;
  border-top: 1px solid #e5ebe8;
  padding-top: 16px;
  color: #5f706a;
  font-size: 13px;
  line-height: 1.55;
}

.dashboard-page .form-note b { color: var(--ink); }
.dashboard-page .result { min-height: 560px; }

.dashboard-page .empty {
  display: grid;
  min-height: 510px;
  place-items: center;
  padding: 32px;
  text-align: center;
}

.dashboard-page .empty-icon {
  display: grid;
  width: 70px;
  height: 70px;
  margin: 0 auto 22px;
  place-items: center;
  border: 1px solid #cad7d2;
  border-radius: 50%;
  background: #f7faf8;
  font-size: 28px;
}

.dashboard-page .empty h3 {
  margin: 0;
  font-size: 20px;
  letter-spacing: -.03em;
}

.dashboard-page .empty p {
  max-width: 42ch;
  margin: 10px auto 0;
  color: var(--muted);
  line-height: 1.6;
}

.dashboard-page .error-box {
  margin: 20px;
  border: 1px solid #e6b4b4;
  background: #fff4f4;
  padding: 16px;
  color: #8c2727;
  font-size: 14px;
  line-height: 1.5;
  overflow-wrap: anywhere;
}

.dashboard-page .error-box a {
  display: inline-block;
  margin-top: 10px;
  font-weight: 800;
}

.dashboard-page .loading {
  display: flex;
  min-height: 510px;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 24px;
  color: var(--muted);
  font-weight: 700;
}

.dashboard-page .spinner {
  width: 22px;
  height: 22px;
  border: 3px solid #dbe3e0;
  border-top-color: var(--ink);
  border-radius: 50%;
  animation: spin .75s linear infinite;
  flex-shrink: 0;
}

.dashboard-page .report { padding: 20px; }

.dashboard-page .score-row {
  display: grid;
  gap: 20px;
  border-bottom: 1px solid var(--line);
  padding-bottom: 22px;
}

.dashboard-page .gauge {
  --score: 0;
  display: grid;
  width: 144px;
  height: 144px;,
  margin: auto;
  place-items: center;
  border-radius: 50%;
  background: conic-gradient(
    var(--gauge-color, var(--green)) calc(var(--score)*1%),
    #e5ebe8 0
  );
  position: relative;
}

.dashboard-page .gauge::after {
  content: "";
  position: absolute;
  width: 112px;
  height: 112px;
  border-radius: 50%;
  background: white;
}

.dashboard-page .gauge-value {
  z-index: 1;
  text-align: center;
}

.dashboard-page .gauge-value strong {
  display: block;
  font-size: 38px;
  letter-spacing: -.07em;
}

.dashboard-page .gauge-value span {
  font-size: 11px;
  color: var(--muted);
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: .1em;
}

.dashboard-page .verdict { align-self: center; }

.dashboard-page .pill {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  border: 1px solid currentColor;
  padding: 6px 9px;
  font-size: 11px;
  font-weight: 900;
  letter-spacing: .08em;
  text-transform: uppercase;
}

.dashboard-page .verdict h3 {
  margin: 12px 0 8px;
  font-size: 26px;
  letter-spacing: -.045em;
}

.dashboard-page .verdict p {
  margin: 0;
  color: var(--muted);
  line-height: 1.58;
}

.dashboard-page .section-title {
  margin: 22px 0 12px;
  font-size: 12px;
  font-weight: 900;
  letter-spacing: .14em;
  text-transform: uppercase;
}

.dashboard-page .checks { display: grid; gap: 9px; }

.dashboard-page .check {
  display: grid;
  grid-template-columns: 34px 1fr;
  gap: 11px;
  border: 1px solid var(--line);
  padding: 13px;
}

.dashboard-page .status-icon {
  display: grid;
  width: 30px;
  height: 30px;
  place-items: center;
  border-radius: 50%;
  font-weight: 900;
}

.dashboard-page .status-pass .status-icon {
  background: #e7f6ee;
  color: var(--green);
}

.dashboard-page .status-caution .status-icon {
  background: #fff0df;
  color: var(--amber);
}

.dashboard-page .status-fail .status-icon {
  background: #fbe7e7;
  color: var(--red);
}

.dashboard-page .check b { font-size: 14px; }

.dashboard-page .check p {
  margin: 4px 0 0;
  color: var(--muted);
  font-size: 13px;
  line-height: 1.45;
}

.dashboard-page .signals {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
}

.dashboard-page .signal {
  border: 1px solid #d5deda;
  background: #f7faf8;
  padding: 6px 8px;
  color: #53625e;
  font-size: 12px;
  overflow-wrap: anywhere;
  max-width: 100%;
}

.dashboard-page .next {
  margin: 0;
  padding: 0;
  list-style: none;
}

.dashboard-page .next li {
  display: grid;
  grid-template-columns: 22px 1fr;
  gap: 9px;
  margin: 10px 0;
  color: #4d5c58;
  font-size: 13px;
  line-height: 1.48;
}

.dashboard-page .next span:first-child {
  display: grid;
  width: 20px;
  height: 20px;
  place-items: center;
  background: var(--lime);
  color: var(--ink);
  font-size: 11px;
  font-weight: 900;
}

.dashboard-page .report-foot {
  margin-top: 20px;
  border-top: 1px solid var(--line);
  padding-top: 15px;
  color: #62726c;
  font-size: 12px;
  line-height: 1.5;
}

.dashboard-page .toast {
  position: fixed;
  right: 20px;
  bottom: 20px;
  z-index: 20;
  max-width: min(360px, calc(100% - 40px));
  border: 1px solid #d5deda;
  background: var(--ink);
  padding: 13px 16px;
  color: white;
  box-shadow: 0 14px 40px rgba(0,0,0,.2);
  font-size: 13px;
  transform: translateY(16px);
  opacity: 0;
  pointer-events: none;
  transition: .18s;
}

.dashboard-page .toast.show {
  transform: none;
  opacity: 1;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (min-width: 700px) {
  .dashboard-page .identity { display: block; }
  .dashboard-page .security-note { display: flex; }
  .dashboard-page .score-row { grid-template-columns: 170px 1fr; }
  .dashboard-page .gauge { margin: 0; }
  .dashboard-page .checks { grid-template-columns: 1fr 1fr; }
}

@media (min-width: 720px) {
  .auth-page .steps { grid-template-columns: repeat(3, 1fr); }
}

@media (min-width: 1020px) {
  .auth-page .stage {
    grid-template-columns: 1.15fr .85fr;
    gap: 80px;
  }

  .auth-page .login-wrap {
    justify-self: end;
    margin: 0;
  }
}

@media (min-width: 1050px) {
  .dashboard-page .workspace {
    grid-template-columns: minmax(0, 1.04fr) minmax(420px, .96fr);
    align-items: start;
  }

  .dashboard-page .result {
    position: sticky;
    top: 92px;
  }
}

@media (max-width: 600px) {
  .auth-page .motto { display: none; }
  .auth-page .stage { padding-top: 32px; }
  .auth-page .corner { display: none; }
  .auth-page .intro { font-size: 18px; }
}

@media (max-width: 560px) {
  .dashboard-page .page {
    width: min(100% - 22px, 1460px);
    padding-top: 22px;
  }

  .dashboard-page .page-head { align-items: start; }

  .dashboard-page .panel-head,
  .dashboard-page .form,
  .dashboard-page .report {
    padding-inline: 15px;
  }

  .dashboard-page .account { gap: 8px; }
  .dashboard-page .logout { padding-inline: 10px; }
  .dashboard-page .avatar { display: none; }
  .dashboard-page .actions > * { width: 100%; }
  .dashboard-page .primary { flex: auto; }
  .dashboard-page .textarea { min-height: 180px; }
}

@media (prefers-reduced-motion: no-preference) {
  .auth-page .stage {
    animation: enter .55s ease-out both;
  }

  @keyframes enter {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: none; }
  }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto !important;
    transition-duration: 0s !important;
    animation-duration: 0s !important;
  }

  .dashboard-page .spinner { animation: none; }
}