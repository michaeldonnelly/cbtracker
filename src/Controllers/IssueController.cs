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
    public class IssueController : Controller
    {
        private readonly ComicBookTrackerContext _context;

        public IssueController(ComicBookTrackerContext context)
        {
            _context = context;
        }

        // GET: Issue
        public async Task<IActionResult> Index(int? authorId, int? seriesId)
        {
            //            int? authorId = 1;
            //          int? seriesId = 43;


            //
            //IQueryable < Issue > comicBookTrackerContext = _context.Issues
            //   .Where(i => i.AuthorId == authorId && i.SeriesId == seriesId)
            //  .Take(25);
            //                .Where(i => (i.AuthorId == authorId) && (i.SeriesId == seriesId))
            //.Include(i => i.Author).Include(i => i.Publisher).Include(i => i.Series);
            //.Where(i => i.SeriesId == seriesId);

            /*
            if (authorId.HasValue)
            {
                comicBookTrackerContext = comicBookTrackerContext.Where(i => i.AuthorId == authorId);
            }
            if (seriesId.HasValue)
            {
                comicBookTrackerContext = comicBookTrackerContext.Where(i => i.SeriesId == seriesId);
            }
            */

            //comicBookTrackerContext = comicBookTrackerContext.Include(i => i.Author).Include(i => i.Publisher).Include(i => i.Series);




            Expression<Func<Issue, bool>> filterLambda = null;
            int resultsToReturn = 500;
            if (authorId.HasValue)
            {
                if (seriesId.HasValue)
                {
                    filterLambda = (i => (i.AuthorId == authorId) && (i.SeriesId == seriesId));
                }
                else
                {
                    filterLambda = (i => i.AuthorId == authorId);
                }
            }
            else
            {
                if (seriesId.HasValue)
                {
                    filterLambda = (i => i.SeriesId == seriesId);
                }
                else
                {
                    filterLambda = (i => true);
                    resultsToReturn = 10;
                }
            }

            // The problem  is that the author sometimes isn't explicit in the DB    AAAAARGH




            var query = _context.Issues
                //.Where(i => (i.AuthorId == authorId) && (i.SeriesId == seriesId))
                //.Where(i => i.Series.AuthorId == authorId)
                .Where(filterLambda)
                .Take(resultsToReturn)
                .Include(i => i.Author)
                .Include(i => i.Series);
    
            string queryString = query.ToQueryString();
            Console.WriteLine(queryString);

            var issueList = await query.ToListAsync();

            return View(issueList);
           //return View(await comicBookTrackerContext.ToListAsync());

        }

        public async Task<IActionResult> Wantlist()
        {
            ViewData["WishList"] = true;
            IQueryable<Issue> query = WantedIssueQuery(recent: false);
            return View(await query.ToListAsync());
        }

        public async Task<IActionResult> PickList()
        {
            ViewData["WishList"] = true;
            IQueryable<Issue> query = WantedIssueQuery(recent: true);
            return View(await query.ToListAsync());
        }


        private IQueryable<Issue> WantedIssueQuery(bool recent)
        { 
            DateTime now = DateTime.Now;
            TimeSpan threeMonths = new TimeSpan(90, 0, 0, 0);
            float currentMonth = now.Year + now.Month / 12;
            float threeMonthsAgo = currentMonth - (3 / 12);

            IQueryable<Issue> query = _context.Issues
                .Where(i => !i.Own && i.Want && !i.MightOwn && !i.MagazineSize);
            if (recent)
            {
                    query = query.Where(i => (i.ReleaseYear + i.ReleaseMonth / 12) >= threeMonthsAgo);

            }
            else
            {
                query = query.Where(i => (i.ReleaseYear + i.ReleaseMonth / 12) < threeMonthsAgo);
            }

            query = query.Include(i => i.Author)
                .Include(i => i.Publisher)
                .Include(i => i.Series);

            return query;
        }

        // GET: Issue/Details/5
        public async Task<IActionResult> Details(long? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var issue = await _context.Issues
                .Include(i => i.Author)
                .Include(i => i.Publisher)
                .Include(i => i.Series)
                .Include(i => i.Tags)
                .FirstOrDefaultAsync(m => m.Id == id);
            if (issue == null)
            {
                return NotFound();
            }

            return View(issue);
        }

        // GET: Issue/Create
        public IActionResult Create()
        {
            ViewData["AuthorId"] = new SelectList(_context.Set<Author>(), "Id", "Id");
            ViewData["PublisherId"] = new SelectList(_context.Set<Publisher>(), "Id", "Id");
            ViewData["SeriesId"] = new SelectList(_context.Set<Series>(), "Id", "Id");
            return View();
        }

        // POST: Issue/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,IssueNumber,Own,ReleaseDay,ReleaseMonth,ReleaseYear,Variant,StoryName,StoryPart,FairPrice,PriceSource,Updated,Created,AuthorId,PublisherId,SeriesId,CoverMonth,CoverYear,Ordered,Want,Annual,ReadingOrder,Special,PullList,MightOwn,MagazineSize")] Issue issue)
        {
            if (ModelState.IsValid)
            {
                _context.Add(issue);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            ViewData["AuthorId"] = new SelectList(_context.Set<Author>(), "Id", "Id", issue.AuthorId);
            ViewData["PublisherId"] = new SelectList(_context.Set<Publisher>(), "Id", "Id", issue.PublisherId);
            ViewData["SeriesId"] = new SelectList(_context.Set<Series>(), "Id", "Id", issue.SeriesId);
            return View(issue);
        }

        // GET: Issue/Edit/5
        public async Task<IActionResult> Edit(long? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var issue = await _context.Issues.FindAsync(id);
            if (issue == null)
            {
                return NotFound();
            }
            ViewData["AuthorId"] = new SelectList(_context.Set<Author>(), "Id", "Id", issue.AuthorId);
            ViewData["PublisherId"] = new SelectList(_context.Set<Publisher>(), "Id", "Id", issue.PublisherId);
            ViewData["SeriesId"] = new SelectList(_context.Set<Series>(), "Id", "Id", issue.SeriesId);
            return View(issue);
        }

        // POST: Issue/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(long id, [Bind("Id,IssueNumber,Own,ReleaseDay,ReleaseMonth,ReleaseYear,Variant,StoryName,StoryPart,FairPrice,PriceSource,Updated,Created,AuthorId,PublisherId,SeriesId,CoverMonth,CoverYear,Ordered,Want,Annual,ReadingOrder,Special,PullList,MightOwn,MagazineSize")] Issue issue)
        {
            if (id != issue.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(issue);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!IssueExists(issue.Id))
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
            ViewData["AuthorId"] = new SelectList(_context.Set<Author>(), "Id", "Id", issue.AuthorId);
            ViewData["PublisherId"] = new SelectList(_context.Set<Publisher>(), "Id", "Id", issue.PublisherId);
            ViewData["SeriesId"] = new SelectList(_context.Set<Series>(), "Id", "Id", issue.SeriesId);
            return View(issue);
        }

        // GET: Issue/Delete/5
        public async Task<IActionResult> Delete(long? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var issue = await _context.Issues
                .Include(i => i.Author)
                .Include(i => i.Publisher)
                .Include(i => i.Series)
                .FirstOrDefaultAsync(m => m.Id == id);
            if (issue == null)
            {
                return NotFound();
            }

            return View(issue);
        }

        // POST: Issue/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(long id)
        {
            var issue = await _context.Issues.FindAsync(id);
            _context.Issues.Remove(issue);
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool IssueExists(long id)
        {
            return _context.Issues.Any(e => e.Id == id);
        }

        public async Task<IActionResult> Buy(long id)
        {
            try
            {
                Issue issue = await _context.Issues.FindAsync(id);
                issue.Own = true;
                await _context.SaveChangesAsync();
                return Content("bought " + id.ToString());
            }
            catch(Exception ex)
            {
                return BadRequest(ex);
            }

        }
    }
}
