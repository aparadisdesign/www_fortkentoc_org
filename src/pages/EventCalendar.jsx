import { Link } from 'react-router-dom'
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'

// Sample events - in production, these would come from an API
const events = [
  {
    title: '2025 Ben Paradis Invitational Relay',
    date: '2025-12-29',
    color: '#2B7DB9'
  },
  {
    title: '2026 Jalbert Youth Ski & Biathlon Program',
    start: '2026-01-03',
    color: '#22c55e'
  },
  {
    title: '2026 Snowshoe Series',
    date: '2026-01-04',
    color: '#8B2332'
  },
  {
    title: '2026 Ladies Ski Nights',
    date: '2026-01-08',
    color: '#F7941D'
  },
  {
    title: '2026 Jalbert Youth Ski & Biathlon Program',
    date: '2026-01-10',
    color: '#22c55e'
  },
  {
    title: '2026 Ladies Ski Nights',
    date: '2026-01-13',
    color: '#F7941D'
  },
  {
    title: '2026 Jalbert Youth Ski & Biathlon Program',
    date: '2026-01-17',
    color: '#22c55e'
  },
  {
    title: '2026 Snowshoe Series',
    date: '2026-01-18',
    color: '#8B2332'
  },
  {
    title: '2026 Ladies Ski Nights',
    date: '2026-01-22',
    color: '#F7941D'
  },
  {
    title: '2026 NorAm Biathlon Event',
    start: '2026-01-23',
    end: '2026-01-26',
    color: '#1E3A5F'
  },
  {
    title: '2026 Ladies Ski Nights',
    date: '2026-01-27',
    color: '#F7941D'
  },
  {
    title: '2026 Jalbert Youth Ski & Biathlon Program',
    date: '2026-01-31',
    color: '#22c55e'
  },
  {
    title: '2026 Snowshoe Series',
    date: '2026-01-31',
    color: '#8B2332'
  },
  {
    title: '2026 Ladies Ski Nights',
    date: '2026-02-05',
    color: '#F7941D'
  }
]

function EventCalendar() {
  return (
    <div className="calendar-page">
      {/* Hero Section */}
      <section className="calendar-hero">
        <div className="hero-overlay">
          <div className="container">
            <div className="calendar-hero-content">
              <h1>Events Calendar</h1>
            </div>
          </div>
        </div>
      </section>

      {/* Calendar Section */}
      <section className="section">
        <div className="container">
          <div className="calendar-wrapper">
            <FullCalendar
              plugins={[dayGridPlugin]}
              initialView="dayGridMonth"
              events={events}
              headerToolbar={{
                left: 'title',
                center: '',
                right: 'today prev,next'
              }}
              height="auto"
              eventDisplay="block"
              dayMaxEvents={3}
            />
          </div>
        </div>
      </section>

      {/* Upcoming Events CTA */}
      <section className="section section-alt">
        <div className="container">
          <div className="centered-content text-center">
            <h2 className="section-title">Want More Details?</h2>
            <p className="content-text">
              Check out our upcoming events page for detailed information about
              each event, registration links, and more.
            </p>
            <Link to="/upcoming-events" className="btn btn-primary">
              View Upcoming Events
            </Link>
          </div>
        </div>
      </section>
    </div>
  )
}

export default EventCalendar
