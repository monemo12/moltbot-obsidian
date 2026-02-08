# Learning System Template v2.0

*A structured framework for designing personalized, evidence-based learning systems.*

---

## 📋 Phase 1: Needs Assessment

### Learning Objectives (Bloom's Taxonomy)
> Define what you want to achieve. Check primary (✅) and secondary (⚠️) goals:

- [ ] **Remembering** - Recall facts, terms, concepts
- [ ] **Understanding** - Explain ideas and principles
- [ ] **Application** - Use knowledge in real situations
- [ ] **Analysis** - Break down and examine components
- [ ] **Evaluation** - Make judgments based on criteria
- [ ] **Creation** - Produce new or original work

**Example:**
- ✅ **Understanding** - Explain core principles and theories
- ✅ **Application** - Apply to real-life observations
- ⚠️ Memory - Remember key terms (secondary goal)

---

### Time & Rhythm
> Realistic time investment and learning schedule:

- **Daily investment:** ___ minutes
- **Duration:** Short-term (<3 months) / Long-term (6+ months)
- **Rhythm:** Intensive (cramming) / Distributed (spaced) ← **Distributed recommended**

---

### Learning Preferences
> How you learn best:

- [ ] Reading text
- [ ] Watching videos
- [ ] Listening to audio
- [ ] Hands-on practice
- [ ] Discussion/teaching others
- [ ] Visual diagrams/mind maps

**Tool selection:**
- SRS (Spaced Repetition): Anki / SuperMemo / Remnote
- Note-taking: Obsidian / Notion / Markdown files
- Video: YouTube / Coursera / Udemy
- Practice: Projects / Exercises / Quizzes

---

### Current Level
> Where are you starting from?

- Complete beginner / Some familiarity / Intermediate / Advanced

---

### Execution Details
> Practical constraints and preferences:

- **Scope:** [Topic name and breadth, e.g., "General Psychology - introductory level"]
- **Success definition:** [How will you know you've succeeded?]
- **Resource language:** [English / Chinese / Mixed]
- **Resource mode:** [AI-generated / Curated / Textbook-based]
- **SRS tool:** [Anki / Other]
- **Reminders:** [Needed / Not needed]
- **Progress check:** [Daily / Weekly / Bi-weekly]
- **Struggle protocol:** [How will you handle difficulties?]
- **Assessment:** [Self-test / Project-based / Quiz]

---

## 🧠 Phase 2: Theoretical Framework

### Selected Learning Theories

| Theory | Application | Tools |
|--------|-------------|-------|
| **Spaced Repetition (SRS)** | Long-term retention | Anki cards |
| **Retrieval Practice** | Strengthen memory | Self-testing |
| **Elaboration** | Deep understanding | Self-explanation prompts |
| **Dual Coding** | Enhance comprehension | Text + visuals |
| **Metacognition** | Monitor progress | Weekly reviews |
| **Interleaving** | Mix topics for better transfer | Varied practice |
| **Concrete Examples** | Ground abstract concepts | Real-world cases |

**Why these theories?**
> Explain why you chose each theory and how it fits your learning objectives.

**Example:**
- SRS: Essential for remembering terms and concepts
- Retrieval: Better than re-reading for understanding
- Elaboration: Supports deep understanding over surface knowledge
- Dual Coding: Matches preference for reading + video
- Metacognition: Weekly check-ins enable adaptive learning

---

## 📖 Phase 2.5: Information Integrity

> **Mandatory for all learning systems:** Ensure content is verifiable and trustworthy.

### Source Requirement Policy

**Every learning material must include:**
1. **Origin** - Where did this information come from?
2. **Type** - Research paper / Textbook / Online article / AI-generated
3. **Access** - Link, ISBN, DOI, or clear citation

**Content classification:**

| Type | Marking | Reliability |
|------|---------|-------------|
| **Peer-reviewed research** | Author, Year, Journal | ⭐⭐⭐⭐⭐ Highest |
| **Academic textbooks** | Author, Edition, Publisher | ⭐⭐⭐⭐ High |
| **Expert-authored articles** | Author, Platform, URL | ⭐⭐⭐ Moderate |
| **Educational videos** | Creator, Platform, URL | ⭐⭐⭐ Moderate |
| **AI-generated (verified)** | [AI] + validation source | ⭐⭐ Low - needs validation |
| **AI-generated (unverified)** | [Unverified] | ⭐ Use with caution |

**Implementation:**
- Add source field to all Anki cards (see 3.4.1)
- Include reference list in learning notes
- Create `resources.md` with full citations
- Use abbreviations for frequently-cited sources

**Example resources.md:**
```markdown
# Resources - [Topic Name]

## Primary Sources
- **[PSY101]** Myers, D.G., & DeWall, C.N. (2021). *Psychology* (14th ed.). Worth Publishers.
- **[SKN53]** Skinner, B.F. (1953). *Science and Human Behavior*. Macmillan.

## Online Resources
- **[CC-PSY]** Crash Course Psychology - https://youtube.com/playlist?list=...
- **[APA]** American Psychological Association - https://www.apa.org/

## AI-Generated Content
- Mark with [AI] tag
- Validate against primary sources when possible
```

**When to challenge a claim:**
- No source provided → Request source
- Source is vague → Request specific citation
- Claim seems unusual → Cross-check with authoritative source

---

## 🏗️ Phase 3: System Components

### 3.1 Learning Path

**Structure:** Choose one:
- Linear: Topic A → Topic B → Topic C
- Modular: Independent units, any order
- Tree: Prerequisites required
- Spiral: Revisit topics at increasing depth

**Example structure:**
```
[Subject Name]
│
├── Module 1: [Topic Name] (X weeks)
│   ├── Unit 1.1: [Subtopic]
│   ├── Unit 1.2: [Subtopic]
│   └── Unit 1.3: [Subtopic]
│   └── ✓ Checkpoint: [What should you be able to do?]
│
├── Module 2: [Topic Name] (X weeks)
│   ├── Unit 2.1: [Subtopic]
│   └── Unit 2.2: [Subtopic]
│   └── ✓ Checkpoint: [Verification criteria]
│
└── Module 3: [Topic Name] (X weeks)
    └── ...
```

**Total duration:** ~X weeks/months at Y min/day

**Prerequisite flow:** Sequential / Parallel / Mixed

---

### 3.2 Daily Routine

> Design your daily learning session. Example:

```
┌─────────────────────────────────────┐
│  X min → Review (Anki/previous)     │
│  Y min → New content (read/watch)   │
│  Z min → Practice (new Anki/quiz)   │
│  W min → Reflection (optional)      │
└─────────────────────────────────────┘
```

**Weekly cycle example:**
- **Sunday evening:** Prepare next week's materials
- **Monday-Friday:** Daily study sessions
- **Saturday:** Weekly review and progress check

---

### 3.3 Anki Card Management (Simplified)

> **Philosophy:** Simple and reliable beats complex automation.

#### System Architecture

```
learning-systems/[topic-name]/anki/
├── week-01.txt              ← Card files (Tab-separated format)
├── week-02.txt
├── create_apkg_v2.py        ← Script to generate .apkg files
└── README.md                ← Usage instructions
```

#### Setup Steps

1. **Create Anki directory:**
```bash
cd learning-systems/[topic-name]
mkdir -p anki
cd anki
```

2. **Copy the generator script:**
```bash
# Copy from psychology-general
cp ~/workspace/learning-systems/psychology-general/anki/create_apkg_v2.py .
chmod +x create_apkg_v2.py
```

#### Card File Format

Create `.txt` files with Tab-separated values (Front[TAB]Back):

```
What is spaced repetition?	A learning technique that spaces reviews over increasing intervals
Define metacognition	Awareness and understanding of one's own thought processes
Who founded behaviorism?	John B. Watson
```

**Best practices:**
- One concept per card
- Use concrete examples
- Keep answers concise
- Use `#` for comments in the file

#### Usage Workflow

**Weekly preparation:**
1. Create `week-XX.txt` with 15-20 new cards
2. Generate `.apkg`: `python3 create_apkg_v2.py week-XX.txt output.apkg`
3. Import the `.apkg` file into Anki (desktop or mobile)

**Daily learning:**
- Open Anki app
- Review cards (spaced repetition handles scheduling automatically)
- Aim for 70-85% retention rate

#### Automation (Optional)

**Option 1: Weekly .apkg delivery via Telegram**
Set up a cron job to auto-generate and send `.apkg` files:

```javascript
// In OpenClaw cron config
{
  "name": "Weekly Anki Cards - [Topic]",
  "schedule": {"kind": "cron", "expr": "0 12 * * 0", "tz": "Asia/Taipei"},
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "Generate .apkg from learning-systems/[topic]/anki/week-*.txt and send to Telegram group using message tool.",
    "deliver": true,
    "channel": "telegram",
    "to": "-5137119242"
  }
}
```

**Option 2: Manual generation on demand**
Just run the script whenever you have new cards ready.

#### Why This Approach?

- ✅ **Reliable:** No complex sync dependencies
- ✅ **Portable:** .apkg files work on any Anki client
- ✅ **Simple:** One script, minimal configuration
- ✅ **Flexible:** Import when you're ready
- ❌ No automatic sync to AnkiWeb (intentional trade-off for simplicity)

**Issue:** Sync doesn't work  
**Fix:** Cards are still saved locally. Sync manually in Anki app.

---

### 3.4 SRS Card System

**Card types:**
1. **Concept cards** - Core definitions
   - Front: "What is [concept]?"
   - Back: Definition + example + **source**

2. **Application cards** - Real-world scenarios
   - Front: "How does [concept] explain [situation]?"
   - Back: Explanation with reasoning + **source**

3. **Distinction cards** - Compare similar concepts
   - Front: "What's the difference between X and Y?"
   - Back: Key distinctions + when to use each + **source**

4. **Process cards** - Step-by-step procedures
   - Front: "How do you [perform task]?"
   - Back: Numbered steps + **source**

**Principles:**
- One concept per card
- Use your own words
- Include concrete examples
- Link to real-life observations
- Avoid yes/no questions (unless testing recall)
- **✅ Always include source/reference** (see Source Standards below)

---

### 3.4.1 Source & Citation Standards

> **Critical:** All learning materials must include verifiable sources.

**Why sources matter:**
- ✅ Builds trust in the information
- ✅ Enables fact-checking and deeper exploration
- ✅ Distinguishes evidence-based content from speculation
- ✅ Provides path for further learning

**Source requirements:**

**For Academic/Scientific Content:**
- Research papers: Author(s), Year, Title, Journal
- Textbooks: Author, Edition, Chapter/Page
- Example: *(Smith & Jones, 2023, "Learning Theory", Journal of Education, Vol. 45)*

**For Online Resources:**
- Website/article: Title + URL
- Video: Platform + Creator + Title + URL
- Course: Platform + Course name + Instructor
- Example: *(Crash Course Psychology #1 - "Intro to Psychology" - https://youtu.be/...)*

**For AI-Generated Content:**
- Mark as **[AI-Generated]** if no external source validates it
- If validated by external sources, cite those instead
- Example: *[AI-Generated - verify with authoritative source before relying on this]*

**Card format with source:**

```
Front: What is operant conditioning?

Back: 
A learning process where behavior is modified by consequences (rewards/punishments).

Example: A dog learns to sit when rewarded with treats.

📚 Source: Skinner, B.F. (1953), "Science and Human Behavior"
```

**Acceptable shortcuts for frequently-used sources:**
- Create abbreviations in `resources.md`
- Example: `[PSY101]` = "Introduction to Psychology, 14th Ed., Myers & DeWall"

**When source is unavailable:**
- Mark as **[Unverified]** or **[AI-Generated]**
- Seek verification before treating as fact
- Update card when source is found

---

### 3.5 Progress Tracking

**File:** `progress.md` in your topic directory

**Tracked metrics:**
- ✅ Units/modules completed
- 📊 Anki stats (retention rate, daily reviews)
- 📝 Weekly reflections
- 🎯 Milestones reached
- 🔧 Adjustments made

**Weekly check format:**
```markdown
### Week N (YYYY-MM-DD to YYYY-MM-DD)

**Completed:**
- Unit X.Y: [Name]
- Anki cards: X new, Y reviewed

**Anki stats:**
- Retention rate: X%
- Daily average: Y cards
- Mature cards: Z

**Reflections:**
- What clicked this week?
- What's still confusing?
- Any real-life applications?
- Energy level: High / Medium / Low

**Adjustments for next week:**
- [If needed: slow down / speed up / change resources]
```

---

## 🔄 Phase 4: Maintenance & Optimization

### Weekly Review Protocol

1. **Check progress file** (or ask directly)
2. **Ask key questions:**
   - How was this week?
   - Any concepts you're struggling with?
   - Anki retention rate?
   - Ready for next unit or need more time?
   - **Are sources clear and accessible?**
3. **Adjust based on feedback:**
   - Content volume
   - Resource mix (more video? different explanations?)
   - Revisit difficult concepts
   - **Source quality** (upgrade AI-generated content with authoritative sources)

### Dynamic Adjustment Signals

**🟢 Accelerate:** (move faster)
- Anki retention >85% consistently
- Concepts are clear
- Eager for more

**🟡 Maintain:** (current pace is good)
- Anki retention 70-85%
- Some concepts need more time
- Comfortable pace

**🔴 Slow down:** (reduce load)
- Anki retention <70%
- Concepts feel overwhelming
- Need consolidation time

**🔵 Pivot:** (change approach)
- Resources aren't clicking
- Need different explanation style
- Interest shifting to specific subtopic

---

## 🎯 Success Criteria

> Define how you'll know the system worked. Example:

By the end of this system, you should be able to:
- ✅ [Objective 1: e.g., Explain core concepts in your own words]
- ✅ [Objective 2: e.g., Apply principles to real situations]
- ✅ [Objective 3: e.g., Understand how research in this field works]
- ✅ [Objective 4: e.g., Have foundation for advanced topics]
- ✅ [Objective 5: e.g., Engage in informed discussions]

---

## 📁 Directory Structure

**Recommended file organization:**

```
learning-systems/
├── INDEX.md                              ← Overview of all learning projects
├── LEARNING_SYSTEM_TEMPLATE.md           ← This template
├── (Automation handled by OpenClaw cron)  ← No local cron setup file
│
└── [topic-name]/                         ← Your learning project
    ├── system.md                         ← Based on this template
    ├── progress.md                       ← Weekly tracking
    ├── resources.md                      ← Study materials
    │
    └── anki/                             ← Anki automation
        ├── week-01.txt
        ├── week-02.txt
        ├── auto_push_sync.py
        ├── push-cards.sh
        └── .ankiweb_config               ← GITIGNORED!
```

**`.gitignore` additions:**
```
# Anki credentials
.ankiweb_config
*.ankiweb_config

# Anki local database
*.anki21
*.anki2
collection.media/
```

---

## 📚 Starting Checklist

When creating a new learning system:

- [ ] Copy this template to `[topic-name]/system.md`
- [ ] Fill in Phase 1 (needs assessment)
- [ ] Select learning theories (Phase 2)
- [ ] Design learning path (Phase 3.1)
- [ ] Set up daily routine (Phase 3.2)
- [ ] Create Anki directory and scripts (Phase 3.3)
- [ ] Create `progress.md` file
- [ ] Create `resources.md` file
- [ ] Prepare Week 1 materials
- [ ] Add to `INDEX.md`

---

## 🔧 Template Variables

Replace these when using the template:

- `[topic-name]` → Your subject (e.g., psychology-general, python-basics)
- `[Subject Name]` → Full name (e.g., General Psychology, Python Programming)
- `X weeks/months` → Your estimated duration
- `Y min/day` → Your daily time commitment
- `[Module/Unit Names]` → Your actual topics
- `YourDeck::SubDeck` → Your Anki deck name

---

*Template version: 2.1*  
*Created: 2026-02-03*  
*Last updated: 2026-02-02*  
*Changelog:*  
- *v2.1 (2026-02-02): Added Phase 2.5 "Information Integrity" with mandatory source citation standards*  
- *v2.0 (2026-02-03): Initial structured template*
