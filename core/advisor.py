# -*- coding: utf-8 -*-
"""
AERO-AGRI Advisor & Recommendation Engine
Builds agricultural adaptation advice ONLY from transparent, computed figures.
Rules:
- Never invent numbers or unfounded conclusions
- Generate a 3-section Markdown report automatically
- call_llm() is a stub that returns None (TODO)
- When call_llm returns None -> fall back to the deterministic template
- lang="en" (default) or "vi": the Vietnamese report is a faithful translation of the English
  template; strategy names, risks and gaps come from each strategy's `vi` block in config/rotations.json
"""
import json

def call_llm(prompt):
    """
    LLM integration (Claude / Gemini / GPT).
    TODO: wire in the provider's API key and SDK for a production deployment.
    For now it returns None so the system uses the safe template fallback.
    """
    return None


# Report wording per language. "en" is the original template; "vi" translates it (no new facts or numbers).
_TEXT = {
    "en": {
        "no_rot": "- No rotation strategy data for this region yet.",
        "table_head": "| Strategy | Supplemental fresh water (m³/ha/year) | If soil percolation is low (m³/ha/year) | Compared with current practice | Bare-soil months |",
        "baseline": "Baseline",
        "cannot_compare": "Cannot compare",
        "shrimp_cell": ", shrimp phase not modeled",
        "not_computed": "Not computed",
        "table_foot": "The main column uses percolation of 4 mm/day; the \"If soil percolation is low\" column uses 2 mm/day. Only rice fields differ. The numbers match the strategy cards in Step 2.",
        "selected": "Selected strategy: **{name}**.",
        "is_current": "This is current practice. The alternative strategies:",
        "risks": "Risks to weigh: {risks}",
        "salinity": "Salinity season according to published documents: months {months}.",
        "water_none": "water not computed",
        "water": "supplemental fresh water {water} m³/ha",
        "water_diff": "supplemental fresh water {water} m³/ha ({sign}{diff} m³/ha vs. current practice)",
        "window": "{label} {start} to {end}",
        "shrimp_line": " Shrimp phase not modeled.",
        "strategy_line": "- **{name}**: {water}. Calendar: {windows}.{partial} To verify before adopting: {gaps}",
        "measure_salinity": "- Measure canal water salinity with a handheld meter before each irrigation intake.",
        "no_data_reason": "not enough data to evaluate",
        "no_data": "### No recommendation yet\n\nReason: **{err}**.\n\nWhat to do: add the NASA POWER data file for this region at `data/raw/power/{region_id}.csv`.",
        "llm_lang": "",
        "synth": "\n> **WARNING:** These results are computed from **SYNTHETIC DEMO DATA**. Load real observed data before using them in the field.\n",
        "scenario": "\n*Simulated scenario:* temperature change `{t} °C`, rainfall change `{r}%`.\n",
        "count_strat": "- Strategies compared: **{n}** (including current practice).",
        "count_crops": "- Crops evaluated: **{n}**.",
        "src_line": "- File `{file}`: {source} ({kind})",
        "src_none": "source not declared",
        "src_synth": "synthetic demo data",
        "src_real": "real observed data",
        "default_question": "Dry-season adaptation assessment",
        "title": "### AERO-AGRI crop transition advisory report",
        "region": "**Region analysed:**",
        "question": "**User question:**",
        "h1": "#### 1. Dry-season data status",
        "sources": "- Data sources loaded:",
        "h2": "#### 2. Whole-year fresh water comparison by strategy",
        "h3": "#### 3. What to do before the next season",
        "note": "*Note: This report is assembled automatically from the FAO-56 Penman-Monteith model and NASA POWER data on a grid of roughly 50 km cells. It does not replace field experience or guidance from local agricultural extension officers.*",
    },
    "vi": {
        "no_rot": "- Vùng này chưa có dữ liệu phương án luân canh.",
        "table_head": "| Phương án | Nước ngọt bổ sung (m³/ha/năm) | Nếu đất thấm ít (m³/ha/năm) | So với hiện trạng | Số tháng đất trống |",
        "baseline": "Mốc so sánh",
        "cannot_compare": "Không so sánh được",
        "shrimp_cell": ", chưa tính giai đoạn nuôi tôm",
        "not_computed": "Chưa tính",
        "table_foot": "Cột chính dùng mức thấm 4 mm/ngày; cột \"Nếu đất thấm ít\" dùng 2 mm/ngày. Chỉ ruộng lúa có khác biệt. Các con số khớp với thẻ phương án ở Bước 2.",
        "selected": "Phương án đã chọn: **{name}**.",
        "is_current": "Đây là cách đang canh tác (hiện trạng). Các phương án thay thế:",
        "risks": "Rủi ro cần cân nhắc: {risks}",
        "salinity": "Mùa mặn theo các văn bản đã công bố: tháng {months}.",
        "water_none": "chưa tính được nước",
        "water": "nước ngọt bổ sung {water} m³/ha",
        "water_diff": "nước ngọt bổ sung {water} m³/ha ({sign}{diff} m³/ha so với hiện trạng)",
        "window": "{label} {start} đến {end}",
        "shrimp_line": " Chưa tính giai đoạn nuôi tôm.",
        "strategy_line": "- **{name}**: {water}. Lịch thời vụ: {windows}.{partial} Cần kiểm chứng trước khi áp dụng: {gaps}",
        "measure_salinity": "- Đo độ mặn nước kênh bằng máy đo cầm tay trước mỗi lần lấy nước vào ruộng.",
        "no_data_reason": "chưa đủ dữ liệu để đánh giá",
        "no_data": "### Chưa có khuyến nghị\n\nLý do: **{err}**.\n\nCần làm: thêm tệp dữ liệu NASA POWER của vùng này tại `data/raw/power/{region_id}.csv`.",
        "llm_lang": "Answer in Vietnamese.\n",
        "synth": "\n> **CẢNH BÁO:** Kết quả này được tính từ **DỮ LIỆU MẪU TỔNG HỢP (DEMO)**. Hãy nạp dữ liệu quan trắc thực trước khi dùng ngoài đồng ruộng.\n",
        "scenario": "\n*Kịch bản mô phỏng:* nhiệt độ thay đổi `{t} °C`, lượng mưa thay đổi `{r}%`.\n",
        "count_strat": "- Số phương án so sánh: **{n}** (kể cả hiện trạng).",
        "count_crops": "- Số cây trồng đã đánh giá: **{n}**.",
        "src_line": "- Tệp `{file}`: {source} ({kind})",
        "src_none": "chưa khai báo nguồn",
        "src_synth": "dữ liệu mẫu tổng hợp",
        "src_real": "dữ liệu quan trắc thực",
        "default_question": "Đánh giá thích ứng mùa khô",
        "title": "### Báo cáo tư vấn chuyển đổi cây trồng AERO-AGRI",
        "region": "**Vùng phân tích:**",
        "question": "**Câu hỏi của người dùng:**",
        "h1": "#### 1. Tình trạng dữ liệu mùa khô",
        "sources": "- Nguồn dữ liệu đã nạp:",
        "h2": "#### 2. So sánh nước ngọt cả năm theo phương án",
        "h3": "#### 3. Việc cần làm trước vụ tới",
        "note": "*Lưu ý: Báo cáo này được tổng hợp tự động từ mô hình FAO-56 Penman-Monteith và dữ liệu NASA POWER trên lưới ô cỡ khoảng 50 km. Báo cáo không thay thế kinh nghiệm thực tế hay hướng dẫn của cán bộ khuyến nông địa phương.*",
    },
}


def _lang(lang):
    """Supported report language; anything else falls back to English."""
    return lang if lang in _TEXT else "en"


def _fmt_int(v, lang="en"):
    """Format a number as an integer with thousands separators: English 15,329, Vietnamese 15.329."""
    s = f"{v:,.0f}"
    return s.replace(",", ".") if lang == "vi" else s


def _fmt_dec(v, fmt, lang="en"):
    """Format a decimal number; Vietnamese uses a decimal comma."""
    s = format(v, fmt)
    return s.replace(".", ",") if lang == "vi" else s


def _vi_block(s, lang):
    return (s.get("vi") or {}) if lang == "vi" else {}


def _name(s, lang="en"):
    """Strategy name: the English `name_vi` field (historical key name), or `vi.name` in Vietnamese."""
    return _vi_block(s, lang).get("name") or s.get("name_vi", s.get("id"))


def _field(s, key, lang="en"):
    """A strategy text list (risks, info_gaps) in the requested language, falling back to English."""
    return _vi_block(s, lang).get(key) or s.get(key)


def _phase_label(p, lang="en"):
    return (lang == "vi" and p.get("label_vi")) or p["label"]


def _day(mmdd, lang="en"):
    """Calendar day: English keeps MM-DD; Vietnamese shows D/M."""
    if lang != "vi":
        return mmdd
    try:
        m, d = (int(x) for x in str(mmdd).split("-"))
    except ValueError:
        return mmdd
    return f"{d}/{m}"


def _sentences(items):
    """Join sentences from config: each one ends with a full stop, separated by a single space."""
    out = []
    for t in items or []:
        t = t.strip()
        if t:
            out.append(t if t.endswith((".", "!", "?")) else t + ".")
    return " ".join(out)


def _rotation_table(rotations, lang="en"):
    """Report section 2: the same whole-year figures as the strategy cards in Step 2."""
    T = _TEXT[_lang(lang)]
    if not rotations or not rotations.get("available"):
        return T["no_rot"]
    strategies = rotations.get("strategies", [])
    base = next((s for s in strategies if s.get("is_existing")), None)
    b = base.get("annual_deficit_mm") if base else None
    rows = [
        T["table_head"],
        "| :--- | ---: | ---: | :--- | ---: |",
    ]
    for s in strategies:
        d = s.get("annual_deficit_mm")
        lo = s.get("annual_deficit_low_mm")
        name = _name(s, lang)
        if s.get("is_existing"):
            cmp = T["baseline"]
        elif d is None or b is None:
            cmp = T["cannot_compare"]
        else:
            diff = (d - b) * 10
            cmp = f"{'+' if diff >= 0 else '−'}{_fmt_int(abs(diff), lang)} m³/ha"
            if s.get("partial"):
                cmp += T["shrimp_cell"]
            elif b > 0:
                pct = round((d - b) / b * 100)
                cmp += f" ({'+' if pct >= 0 else '−'}{abs(pct)}%)"
        water = T["not_computed"] if d is None else _fmt_int(d * 10, lang)
        low = "–" if lo is None else _fmt_int(lo * 10, lang)
        rows.append(f"| {name} | {water} | {low} | {cmp} | {len(s.get('bare_months') or [])} |")
    rows.append("")
    rows.append(T["table_foot"])
    return "\n".join(rows)


def _rotation_actions(rotations, strategy_id=None, lang="en"):
    """Report section 3: list each alternative strategy, using only figures and wording already in rotations."""
    T = _TEXT[_lang(lang)]
    if not rotations or not rotations.get("available"):
        return T["no_rot"]
    strategies = rotations.get("strategies", [])
    base = next((s for s in strategies if s.get("is_existing")), None)
    base_def = base.get("annual_deficit_mm") if base else None
    lines = []
    picked = next((s for s in strategies if s.get("id") == strategy_id), None) if strategy_id else None
    if picked is not None:
        lines.append(T["selected"].format(name=_name(picked, lang)))
        if picked.get("is_existing"):
            lines.append(T["is_current"])
        else:
            risks = _sentences(_field(picked, "risks", lang))
            if risks:
                lines.append(T["risks"].format(risks=risks))
            strategies = [picked] + [s for s in strategies if s is not picked]
    sal = rotations.get("salinity_months") or []
    if sal:
        lines.append(T["salinity"].format(months=", ".join(str(m) for m in sal)))
    for s in strategies:
        if s.get("is_existing"):
            continue
        d = s.get("annual_deficit_mm")
        if d is None:
            water = T["water_none"]
        elif base_def is None:
            water = T["water"].format(water=_fmt_int(d * 10, lang))
        else:
            diff = (d - base_def) * 10
            sign = "+" if diff >= 0 else "−"
            water = T["water_diff"].format(water=_fmt_int(d * 10, lang), sign=sign,
                                           diff=_fmt_int(abs(diff), lang))
        windows = "; ".join(
            T["window"].format(label=_phase_label(p, lang), start=_day(p["window"]["start"], lang),
                               end=_day(p["window"]["end"], lang))
            for p in s.get("phases", [])
            if p.get("window") and p["window"].get("start")
        )
        partial = T["shrimp_line"] if s.get("partial") else ""
        gaps = _sentences(_field(s, "info_gaps", lang))
        lines.append(T["strategy_line"].format(name=_name(s, lang), water=water, windows=windows,
                                               partial=partial, gaps=gaps))
    if sal:
        lines.append(T["measure_salinity"])
    return "\n".join(lines)


def build_advice(region_id, eval_results, question="", rotations=None, strategy_id=None, lang="en"):
    """
    Build the 3-section Markdown advice entirely from the figures in eval_results and rotations.
    `lang`: "en" (default) or "vi"; any other value gives English.
    """
    lang = _lang(lang)
    T = _TEXT[lang]
    if not eval_results or not eval_results.get("available"):
        err_msg = (eval_results or {}).get("error", T["no_data_reason"])
        return {
            "markdown": T["no_data"].format(err=err_msg, region_id=region_id),
            "used_llm": False
        }

    reg_name = eval_results.get("region_name", region_id)
    if lang == "vi":
        reg_name = ((rotations or {}).get("vi") or {}).get("region_name") or reg_name
    crops = eval_results.get("crops", [])
    sim = eval_results.get("simulation", {})
    is_synthetic = eval_results.get("is_synthetic", False)

    # 1. Prepare the LLM prompt
    prompt = f"""You are the AERO-AGRI agricultural advisor. Answer the question: "{question}" for the region {reg_name}.
CORE RULE: Use only the figures in the JSON below; do not invent any information beyond the data provided.
{T['llm_lang']}EVALUATION JSON DATA:
{json.dumps(eval_results, ensure_ascii=False, indent=2)}
"""

    llm_resp = call_llm(prompt)
    if llm_resp:
        return {"markdown": llm_resp, "used_llm": True}

    # 2. Build the text from the deterministic numeric template
    # Section 1: data status
    synth_banner = T["synth"] if is_synthetic else ""

    sim_note = ""
    d_temp = sim.get("delta_temp_c", 0.0)
    d_rain = sim.get("delta_rain_pct", 0.0)
    if d_temp != 0.0 or d_rain != 0.0:
        sim_note = T["scenario"].format(t=_fmt_dec(d_temp, "+.1f", lang), r=_fmt_dec(d_rain, "+.0f", lang))

    # Section 2: whole-year comparison table by rotation strategy
    table_md = _rotation_table(rotations, lang)
    n_strat = len(rotations.get("strategies", [])) if rotations and rotations.get("available") else 0
    count_line = T["count_strat"].format(n=n_strat) if n_strat else T["count_crops"].format(n=len(crops))

    # Section 3: what to do before the next season
    actions_md = _rotation_actions(rotations, strategy_id, lang)

    # Data source notes (source names and citations stay in their original language)
    src_lines = []
    for d in eval_results.get("data_used", []):
        kind = T["src_synth"] if d.get("is_synthetic") else T["src_real"]
        src_lines.append(T["src_line"].format(file=d.get("file", "N/A"), source=d.get("source", T["src_none"]),
                                              kind=kind))
    sources_block = "\n".join(src_lines)

    markdown = f"""{T['title']}
{T['region']} {reg_name}
{T['question']} *"{question if question else T['default_question']}"*
{synth_banner}{sim_note}
---

{T['h1']}
{count_line}
{T['sources']}
{sources_block}

---

{T['h2']}

{table_md}

---

{T['h3']}
{actions_md}

---
{T['note']}
"""

    return {
        "markdown": markdown.strip(),
        "used_llm": False
    }
