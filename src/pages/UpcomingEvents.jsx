const PdfIcon = () => (
  <svg className="pdf-icon" viewBox="0 0 384 512" fill="currentColor">
    <path d="M181.9 256.1c-5-16-4.9-46.9-2-46.9 8.4 0 7.6 36.9 2 46.9zm-1.7 47.2c-7.7 20.2-17.3 43.3-28.4 62.7 18.3-7 39-17.2 62.9-21.9-12.7-9.6-24.9-23.4-34.5-40.8zM86.1 428.1c0 .8 13.2-5.4 34.9-40.2-6.7 6.3-29.1 24.5-34.9 40.2zM248 160h136v328c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V24C0 10.7 10.7 0 24 0h200v136c0 13.2 10.8 24 24 24zm-8 171.8c-20-12.2-33.3-29-42.7-53.8 4.5-18.5 11.6-46.6 6.2-64.2-4.7-29.4-42.4-26.5-47.8-6.8-5 18.3-.4 44.1 8.1 77-11.6 27.6-28.7 64.6-40.8 85.8-.1 0-.1.1-.2.1-27.1 13.9-73.6 44.5-54.5 68 5.6 6.9 16 10 21.5 10 17.9 0 35.7-18 61.1-61.8 25.8-8.5 54.1-19.1 79-23.2 21.7 11.8 47.1 19.5 64 19.5 29.2 0 31.2-32 19.7-43.4-13.9-13.6-54.3-9.7-73.6-7.2zM377 105L279 7c-4.5-4.5-10.6-7-17-7h-6v128h128v-6.1c0-6.3-2.5-12.4-7-16.9zm-74.1 255.3c4.1-2.7-2.5-11.9-42.8-9 37.1 15.8 42.8 9 42.8 9z"/>
  </svg>
)

const events = [
  {
    title: '2026 Jalbert Youth Ski & Biathlon Program',
    dates: [
      { date: 'January 3, 2026', time: '1:00 PM – 2:00 PM' },
      { date: 'January 10, 2026', time: '1:00 PM – 2:00 PM' },
      { date: 'January 17, 2026', time: '1:00 PM – 2:00 PM' },
      { date: 'January 31, 2026', time: '1:00 PM – 2:00 PM' },
      { date: 'February 14, 2026', time: '1:00 PM – 2:00 PM' }
    ],
    pdf: null
  },
  {
    title: '2025 Ben Paradis Invitational Relay',
    dates: [
      { date: 'December 29, 2025', time: '9:00 AM – 1:00 PM' }
    ],
    pdf: null
  },
  {
    title: "2026 Women's Wellness Day",
    dates: [
      { date: 'March 7, 2026', time: '8:00 AM – 3:00 PM' }
    ],
    pdf: null
  },
  {
    title: '2026 NorAm Biathlon Event',
    dates: [
      { date: 'January 23, 2026', time: '8:00 AM – 1:00 PM' },
      { date: 'January 24, 2026', time: '8:00 AM – 1:00 PM' },
      { date: 'January 25, 2026', time: '8:00 AM – 1:00 PM' }
    ],
    pdf: null
  },
  {
    title: '2026 Ladies Ski Nights',
    dates: [
      { date: 'January 8, 2026', time: '6:30 PM' },
      { date: 'January 13, 2026', time: '6:30 PM' },
      { date: 'January 22, 2026', time: '6:30 PM' },
      { date: 'January 27, 2026', time: '6:30 PM' },
      { date: 'February 5, 2026', time: '6:30 PM' },
      { date: 'February 10, 2026', time: '6:30 PM' }
    ],
    pdf: 'https://www.fortkentoc.org/static/2026LadiesSkiNightsPoster.pdf'
  },
  {
    title: '2026 Snowshoe Series',
    dates: [
      { date: 'January 4, 2026', time: '1:00 PM – 2:30 PM' },
      { date: 'January 18, 2026', time: '1:00 PM – 2:30 PM' },
      { date: 'January 31, 2026', time: '6:30 PM – 8:00 PM' },
      { date: 'February 8, 2026', time: '1:00 PM – 2:30 PM' },
      { date: 'February 21, 2026', time: '6:30 PM – 8:00 PM' },
      { date: 'March 15, 2026', time: '1:30 PM – 2:30 PM' }
    ],
    pdf: null
  }
]

function UpcomingEvents() {
  return (
    <div className="events-page">
      {/* Hero Section */}
      <section className="events-hero">
        <div className="hero-overlay">
          <div className="container">
            <div className="events-hero-content">
              <h1>Upcoming Events</h1>
              <p>
                The Fort Kent Outdoor Center promotes healthy outdoor lifestyles by providing
                a first-rate facility, outdoor trail system, and recreational activities for
                members, athletes, and visitors.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Events Grid Section */}
      <section className="section">
        <div className="container">
          <div className="events-grid">
            {events.map((event, index) => (
              <article key={index} className="event-card">
                <h2 className="event-title">{event.title}</h2>
                <div className="event-dates">
                  <strong>Event Date(s):</strong>
                  {event.dates.map((dateInfo, idx) => (
                    <div key={idx} className="event-date-row">
                      <span className="event-date">{dateInfo.date}</span>
                      <span className="event-time">{dateInfo.time}</span>
                    </div>
                  ))}
                </div>
                {event.pdf && (
                  <a
                    href={event.pdf}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="event-pdf-link"
                  >
                    <PdfIcon />
                    View Event PDF
                  </a>
                )}
              </article>
            ))}
          </div>
        </div>
      </section>
    </div>
  )
}

export default UpcomingEvents
