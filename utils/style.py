import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* ==============================
           MAIN APPLICATION
        ============================== */

        .stApp {
            background:
                radial-gradient(
                    circle at 10% 10%,
                    rgba(79, 70, 229, 0.18),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 90% 20%,
                    rgba(59, 130, 246, 0.14),
                    transparent 30%
                ),
                #0b1020;
        }


        /* ==============================
           SIDEBAR
        ============================== */

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    180deg,
                    #111827 0%,
                    #0b1020 100%
                );
            border-right: 1px solid rgba(255,255,255,0.08);
        }


        [data-testid="stSidebar"] * {
            color: #f8fafc;
        }


        /* ==============================
           MAIN CONTENT
        ============================== */

        .block-container {
            max-width: 1250px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }


        /* ==============================
           HEADINGS
        ============================== */

        h1 {
            font-weight: 800 !important;
            letter-spacing: -1px;
        }


        h2 {
            font-weight: 700 !important;
        }


        h3 {
            font-weight: 650 !important;
        }


        /* ==============================
           HERO
        ============================== */

        .hero {
            padding: 45px;
            border-radius: 28px;
            margin-bottom: 30px;

            background:
                linear-gradient(
                    135deg,
                    rgba(79,70,229,0.95),
                    rgba(37,99,235,0.85),
                    rgba(14,165,233,0.75)
                );

            box-shadow:
                0 25px 60px rgba(0,0,0,0.35);

            border: 1px solid rgba(255,255,255,0.15);
        }


        .hero-small {
            color: rgba(255,255,255,0.8);
            font-size: 15px;
            margin-bottom: 10px;
        }


        .hero-title {
            color: white;
            font-size: 46px;
            font-weight: 850;
            line-height: 1.1;
            margin-bottom: 15px;
        }


        .hero-text {
            color: rgba(255,255,255,0.88);
            font-size: 18px;
            max-width: 750px;
            line-height: 1.6;
        }


        /* ==============================
           CARDS
        ============================== */

        .feature-card {
            background:
                linear-gradient(
                    145deg,
                    rgba(30,41,59,0.95),
                    rgba(15,23,42,0.95)
                );

            border: 1px solid rgba(255,255,255,0.08);

            border-radius: 20px;

            padding: 25px;

            min-height: 190px;

            box-shadow:
                0 12px 30px rgba(0,0,0,0.22);

            transition:
                transform 0.2s ease,
                border-color 0.2s ease;
        }


        .feature-card:hover {
            transform: translateY(-4px);

            border-color:
                rgba(99,102,241,0.55);
        }


        .feature-icon {
            font-size: 34px;
            margin-bottom: 10px;
        }


        .feature-title {
            color: white;
            font-size: 21px;
            font-weight: 750;
            margin-bottom: 8px;
        }


        .feature-text {
            color: #cbd5e1;
            font-size: 14px;
            line-height: 1.6;
        }


        /* ==============================
           STAT CARDS
        ============================== */

        .stat-card {
            background:
                rgba(15,23,42,0.88);

            border:
                1px solid rgba(255,255,255,0.08);

            border-radius: 18px;

            padding: 22px;

            text-align: center;

            box-shadow:
                0 10px 25px rgba(0,0,0,0.18);
        }


        .stat-number {
            color: white;
            font-size: 30px;
            font-weight: 800;
        }


        .stat-label {
            color: #94a3b8;
            font-size: 13px;
            margin-top: 5px;
        }


        /* ==============================
           SECTION LABEL
        ============================== */

        .section-label {
            color: #a5b4fc;
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 8px;
        }


        /* ==============================
           INSIGHT CARD
        ============================== */

        .insight-card {
            background:
                linear-gradient(
                    135deg,
                    rgba(30,41,59,0.95),
                    rgba(49,46,129,0.35)
                );

            border:
                1px solid rgba(129,140,248,0.25);

            border-radius: 20px;

            padding: 25px;

            margin-top: 20px;
        }


        .insight-title {
            color: white;
            font-size: 20px;
            font-weight: 750;
        }


        .insight-text {
            color: #cbd5e1;
            line-height: 1.6;
        }


        /* ==============================
           BUTTONS
        ============================== */

        .stButton > button {
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.12);

            padding: 0.65rem 1.2rem;

            font-weight: 650;

            transition:
                transform 0.15s ease,
                box-shadow 0.15s ease;
        }


        .stButton > button:hover {
            transform: translateY(-2px);

            box-shadow:
                0 8px 20px rgba(0,0,0,0.25);
        }


        /* ==============================
           INPUTS
        ============================== */

        input,
        textarea {
            border-radius: 12px !important;
        }


        /* ==============================
           DIVIDER
        ============================== */

        hr {
            border-color:
                rgba(255,255,255,0.08) !important;
        }


        /* ==============================
           FOOTER
        ============================== */

        .footer {
            text-align: center;
            color: #64748b;
            font-size: 13px;
            margin-top: 50px;
            padding-top: 20px;
            border-top:
                1px solid rgba(255,255,255,0.06);
        }

        </style>
        """,
        unsafe_allow_html=True
    )
