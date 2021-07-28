using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using ComicBookTracker;
using ComicBookTracker.Models;

namespace ComicBookTracker.Controllers
{
    public class TradeController : Controller
    {
        private readonly ComicBookTrackerContext _context;

        public TradeController(ComicBookTrackerContext context)
        {
            _context = context;
        }

        // GET: Trade
        public async Task<IActionResult> Index()
        {
            var comicBookTrackerContext = _context.Trades.Include(t => t.Series);
            return View(await comicBookTrackerContext.ToListAsync());
        }

        // GET: Trade/Details/5
        public async Task<IActionResult> Details(long? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var trade = await _context.Trades
                .Include(t => t.Series)
                .FirstOrDefaultAsync(m => m.Id == id);
            if (trade == null)
            {
                return NotFound();
            }

            return View(trade);
        }

        // GET: Trade/Create
        public IActionResult Create()
        {
            ViewData["SeriesId"] = new SelectList(_context.Set<Series>(), "Id", "Id");
            return View();
        }

        // POST: Trade/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Volume,Own,Title,ReleaseMonth,ReleaseYear,Binding,SeriesId")] Trade trade)
        {
            if (ModelState.IsValid)
            {
                _context.Add(trade);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            ViewData["SeriesId"] = new SelectList(_context.Set<Series>(), "Id", "Id", trade.SeriesId);
            return View(trade);
        }

        // GET: Trade/Edit/5
        public async Task<IActionResult> Edit(long? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var trade = await _context.Trades.FindAsync(id);
            if (trade == null)
            {
                return NotFound();
            }
            ViewData["SeriesId"] = new SelectList(_context.Set<Series>(), "Id", "Id", trade.SeriesId);
            return View(trade);
        }

        // POST: Trade/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(long id, [Bind("Id,Volume,Own,Title,ReleaseMonth,ReleaseYear,Binding,SeriesId")] Trade trade)
        {
            if (id != trade.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(trade);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!TradeExists(trade.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            ViewData["SeriesId"] = new SelectList(_context.Set<Series>(), "Id", "Id", trade.SeriesId);
            return View(trade);
        }

        // GET: Trade/Delete/5
        public async Task<IActionResult> Delete(long? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var trade = await _context.Trades
                .Include(t => t.Series)
                .FirstOrDefaultAsync(m => m.Id == id);
            if (trade == null)
            {
                return NotFound();
            }

            return View(trade);
        }

        // POST: Trade/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(long id)
        {
            var trade = await _context.Trades.FindAsync(id);
            _context.Trades.Remove(trade);
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool TradeExists(long id)
        {
            return _context.Trades.Any(e => e.Id == id);
        }
    }
}
