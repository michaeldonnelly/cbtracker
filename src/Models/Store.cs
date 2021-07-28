using System;
using System.Collections.Generic;

#nullable disable

namespace ComicBookTracker.Models
{
    public partial class Store
    {
        public long Id { get; set; }
        public string Name { get; set; }
        public string MetroArea { get; set; }
        public string Address { get; set; }
        public long? BackIssueBins { get; set; }
        public long? BackIssueOrganization { get; set; }
        public long? BackIssuePrice { get; set; }
        public byte[] HasBronzeAge { get; set; }
        public byte[] HasIndie { get; set; }
        public long? DollarBins { get; set; }
        public long? DollarBinOrganization { get; set; }
        public string Notes { get; set; }
    }
}
