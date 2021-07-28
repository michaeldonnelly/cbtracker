using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using ComicBookTracker;
using ComicBookTracker.Models;
using System.Linq.Expressions;

namespace ComicBookTracker.Controllers
{
    public class SeriesController : Controller
    {
        private readonly ComicBookTrackerContext _context;

        public SeriesController(ComicBookTrackerContext context)
        {
            _context = context;
        }

        // GET: Series
        public async Task<IActionResult> Index(bool currentOnly = false)
        {
            DbSet <Series> series = _context.Series;
            Expression<Func<Series, bool>> predicate = null;
            if (currentOnly)
            {
                predicate = s => s.Current;
            }

            IOrderedQueryable<Series> comicBookTrackerContext = series.Include(s => s.Author).Include(s => s.Publisher).OrderBy(s => s.SortName);

            if (predicate != null)
            {
                comicBookTrackerContext = (IOrderedQueryable<Series>)comicBookTrackerContext.Where(predicate);
            }
            return View(await comicBookTrackerContext.ToListAsync());
        }

   

        public async Task<IActionResult> Current()
        {
            var comicBookTrackerContext = _context.Series.Where(s => s.Current)
                .OrderBy(s => s.SortName).Include(s => s.Author).Include(s => s.Publisher);
            return View(await comicBookTrackerContext.ToListAsync());
        }

        // GET: Series/Details/5
        public async Task<IActionResult> Details(long? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var series = await _context.Series
                .Include(s => s.Author)
                .Include(s => s.Publisher)
                .FirstOrDefaultAsync(m => m.Id == id);
            if (series == null)
            {
                return NotFound();
            }

            return View(series);
        }

        // GET: Series/Create
        public IActionResult Create()
        {
            ViewData["AuthorId"] = new SelectList(_context.Authors, "Id", "Id");
            ViewData["PublisherId"] = new SelectList(_context.Publishers, "Id", "Id");
            return View();
        }

        // POST: Series/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Name,Volume,StartYear,Current,Updated,Created,AuthorId,PublisherId,SortName,PullList")] Series series)
        {
            if (ModelState.IsValid)
            {
                _context.Add(series);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            ViewData["AuthorId"] = new SelectList(_context.Authors, "Id", "Id", series.AuthorId);
            ViewData["PublisherId"] = new SelectList(_context.Publishers, "Id", "Id", series.PublisherId);
            return View(series);
        }

        // GET: Series/Edit/5
        public async Task<IActionResult> Edit(long? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var series = await _context.Series.FindAsync(id);
            if (series == null)
            {
                return NotFound();
            }
            ViewData["AuthorId"] = new SelectList(_context.Authors, "Id", "Id", series.AuthorId);
            ViewData["PublisherId"] = new SelectList(_context.Publishers, "Id", "Id", series.PublisherId);
            return View(series);
        }

        // POST: Series/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(long id, [Bind("Id,Name,Volume,StartYear,Current,Updated,Created,AuthorId,PublisherId,SortName,PullList")] Series series)
        {
            if (id != series.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(series);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!SeriesExists(series.Id))
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
            ViewData["AuthorId"] = new SelectList(_context.Authors, "Id", "Id", series.AuthorId);
            ViewData["PublisherId"] = new SelectList(_context.Publishers, "Id", "Id", series.PublisherId);
            return View(series);
        }

        // GET: Series/Delete/5
        public async Task<IActionResult> Delete(long? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var series = await _context.Series
                .Include(s => s.Author)
                .Include(s => s.Publisher)
                .FirstOrDefaultAsync(m => m.Id == id);
            if (series == null)
            {
                return NotFound();
            }

            return View(series);
        }

        // POST: Series/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(long id)
        {
            var series = await _context.Series.FindAsync(id);
            _context.Series.Remove(series);
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool SeriesExists(long id)
        {
            return _context.Series.Any(e => e.Id == id);
        }
    }
}
