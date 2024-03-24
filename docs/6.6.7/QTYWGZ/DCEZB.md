<p>大商所期权上市后，为了更好的服务市场，大商所启动了期权六期项目，主要从行权功能优化、期权套保、组合保证金优惠三方面完善期权相关业务。</p>
<p>大商所目前支持的组合有：期货对锁，期货跨期，期货跨品种，备兑买权，备兑卖权，期权跨式，期权宽跨式共7种，投保标志支持投机-投机，套保-套保，投机-套保，套保-投机共4种。</p>
<p>本文主要就API针对组保业务的一些调整和特性做相关说明，具体业务规则请参考交易所文档。</p>
<span class="anchor" id="24a47737-4743-4785-9270-09b25200c0a9"></span>
## 1.接口说明
<p>录入请求：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQCOMBACTIONINSERT/">ReqCombActionInsert</a></p>
<p>错误响应：<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONERRRTNCOMBACTIONINSERT/">OnErrRtnCombActionInsert</a>，<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPCOMBACTIONINSERT/">OnRspCombActionInsert</a></p>
<p>正确响应：<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNCOMBACTION/">OnRtnCombAction</a></p>
<blockquote>
<p>注意，这些接口并非新增，而是大商所的组合业务复用了此接口。</p>
</blockquote>
<span class="anchor" id="64c593d4-afa7-413c-adad-4e7a9ceae256"></span>
## 2.可申请组合的合约
<p>组合和拆分的合约为大商所组合优惠表中所列的合约，但目前CTP暂时不支持此优惠表的查询。在实际操作中，用户可通过<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINSTRUMENT/">OnRspQryInstrument</a>或<a href="../../HQJK/CTHOSTFTDCMDSPI/ONRTNDEPTHMARKETDATA/">OnRtnDepthMarketData</a>里返回的组合合约来填写。</p>
<blockquote>
<p>目前的套利单合约（期货跨期和跨品种）基本都在大商所组合优惠表中。但是有一种情况，就是新合约上市，套利合约也是新合约的时候，当天是不包括在组合优惠表中的。</p>
</blockquote>
<span class="anchor" id="008550ee-fd1d-42b5-992a-363e9623a481"></span>
## 3.申请组合填写规则
<ul>
<li>合约（InstrumentID）：</li>
</ul>
<p>针对各组合类型举例如下：</p>
<p>a)  期权跨式组合合约申请和拆分（STD m1905-c-2700&amp;m1905-p-2700）</p>
<p>b)  期权宽跨式组合合约申请和拆分（STG m1905-p-2400&amp;m1905-c-2700）</p>
<p>c)  备兑组合合约申请和拆分（PRT m1905-c-2400&amp;m1905）</p>
<p>d)  期货跨期组合合约申请和拆分（SP a1903&amp;a1905）</p>
<p>e)  期货跨品种组合合约申请和拆分（SPC c1903&amp;cs1909）</p>
<p>f)  期货对锁组合合约申请和拆分（SP a1903&amp; a1903）</p>
<p>g)  期权买入垂直价差组合（BLS m1809-P-3150&amp;m1809-P-3100）</p>
<p>h)  期权卖出垂直价差组合（BES m1809-P-3350&amp;m1809-P-3150）</p>
<p>i)  期权日历价差组合（CAS m1807-P-3150&amp;m1809-P-3150）</p>
<p>j)  买入期权期货组合（BFO m1809-P-3150&amp;m1809）</p>
<p>k)  期权对锁组合合约申请和拆分（OPL m1809-P-3150&amp;m1809-P-3150）</p>
<ul>
<li>买卖方向（Direction）</li>
</ul>
<p>以上面所列组合类型为例：</p>
<p>a、  b：方向为卖。这种组合类型需要左右两腿都是卖持仓，即空头持仓；</p>
<p>c：方向为卖。因为目前交易所只支持备兑卖权，不支持备兑买权，即支持左腿是卖持仓的组合，不支持左腿是买持仓的组合。</p>
<p>若右腿组合的是多头的期货合约，则称为“备兑看涨期权组合持仓”；若右腿组合的是空头的期货合约，则称为“备兑看跌期权组合持仓”；</p>
<p>d、e：当方向是买的时候就是左买持右卖持，当方向是卖的时候就是左卖持右买持；</p>
<p>f：方向只支持买，所以是只有左买持右卖持。</p>
<p>g：买入垂直价差组合：当方向是买时就是左买持仓右卖持，若为卖则会报错“CTP:找不到合约”</p>
<p>h：卖出垂直价差组合：当方向是卖时就是左卖持仓右买持，若为买则会报错“CTP:找不到合约”</p>
<p>i：日历价差：</p>
<p>1）卖出较近月份的看涨期权合约，买入较远月份相同执行价格的看涨期权合约，组合的买卖方向为卖</p>
<p>2）卖出较近月份的看跌期权合约，买入较远月份相同执行价格的看跌期权合约，组合的买卖方向为卖</p>
<p>j：买入期权期货组合：组合买卖方向为买</p>
<p>1）买入看涨期权，同时卖出对应期货合约</p>
<p>2）买入看跌期权，同时买入对应期货合约</p>
<p>k：期权对锁组合：组合买卖方向为买</p>
<p>1）在同一期权品种同一系列同一合约上建立数量相等、方向相反的头寸</p>
<ul>
<li>组合方向（CombDirection）</li>
</ul>
<p>组合方向支持‘申请组合’和‘拆分组合’。</p>
<ul>
<li>投机套保类型（HedgeFlag）</li>
</ul>
<p>投机套保类型支持‘投机’（指左右两腿都是投机），‘保值’（指左右两腿都是套保），‘投套（指左腿投机右腿套保）’，‘套投（指左腿套保右腿投机）’。</p>
<blockquote>
<p>盘中的话，如果通过套利报单的话（<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a>），是只支持投机-投机，套保-套保；如果是通过申请组合形成组合单的话，支持投机-投机，套保-套保，投机-套保，套保-投机。</p>
</blockquote>
<ul>
<li>交易所（ExchangeID）</li>
</ul>
<p>该字段必填。</p>
<span class="anchor" id="1ca4ee42-30f7-445e-a53b-fd0ce74dae62"></span>
## 4.仓位计算规则
<p>组合合约申请接受后，会将现有的两腿持仓组合到一起，形成组合持仓。此时，在持仓汇总（<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITION/">OnRspQryInvestorPosition</a>）里会显示三条持仓记录，分别是新增的组合合约持仓，原多头合约持仓和原空头合约持仓。而持仓明细（<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITIONDETAIL/">OnRspQryInvestorPositionDetail</a>）里不会新增组合合约记录。</p>
<p>1)  比如投资者在大商所买入1手“SP a0905&amp;a0909”合约，形成的持仓汇总如下：</p>
<table><tr><th style="TEXT-ALIGN: center;">合约</th><th style="TEXT-ALIGN: center;">多头持仓</th><th style="TEXT-ALIGN: center;">空头持仓</th></tr><tr><td style="TEXT-ALIGN: center;">SP a0905&amp;a0909</td>
<td style="TEXT-ALIGN: center;">1</td>
<td style="TEXT-ALIGN: center;">0</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">a0905</td>
<td style="TEXT-ALIGN: center;">1</td>
<td style="TEXT-ALIGN: center;">0</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">a0909</td>
<td style="TEXT-ALIGN: center;">1</td>
<td style="TEXT-ALIGN: center;">0</td>
</tr>
</table>
<p>2)  比如投资者在大商所组合1手“STG c1909-P-1680&amp;c1909-C-2020”合约，形成的持仓汇总如下：</p>
<table><tr><th style="TEXT-ALIGN: center;">合约</th><th style="TEXT-ALIGN: center;">多头持仓</th><th style="TEXT-ALIGN: center;">空头持仓</th></tr><tr><td style="TEXT-ALIGN: center;">STG c1909-P-1680&amp;c1909-C-2020</td>
<td style="TEXT-ALIGN: center;">0</td>
<td style="TEXT-ALIGN: center;">1</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">c1909-P-1680</td>
<td style="TEXT-ALIGN: center;">0</td>
<td style="TEXT-ALIGN: center;">1</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">c1909-C-2020</td>
<td style="TEXT-ALIGN: center;">0</td>
<td style="TEXT-ALIGN: center;">1</td>
</tr>
</table>
<span class="anchor" id="c9aab28d-6b94-45bd-a99d-143230e6bdf8"></span>
## 5.平仓盈亏计算和保证金释放计算原则
<p>平仓盈亏计算和保证金释放计算原则如下：</p>
<p>1）在计算平仓盈亏时，采用先开先平原则。</p>
<p>2）在计算保证金释放时，采用先平单腿持仓，后平优惠组合持仓的原则，优惠组合按照优先级从低到高的顺序进行打破。</p>
<p>3）投资者持仓明细里面的TimeFirstVolume（大商所专用）是指大商所的持仓按照先开先平的平仓顺序平仓后的剩余手数</p>
<p>4）投资者持仓明细里面的Volume如果是大商所的持仓则按照先单一后组合的平仓顺序平仓后的剩余手数</p>
<p>5）投资者持仓接口里面的PositionCostOffset，因为目前大商所平仓还是按照先单一后组合进行平仓，而计算平仓盈亏需要按照先开先平进行计算，所以增加该字段用以计算按照先开先平的原则的持仓盈亏。</p>
<p>综上所述，在通过持仓明细去计算持仓成本、持仓盈亏、平仓盈亏时，需要用TimeFirstVolume；计算保证金时，需要用Volume。</p>
<p>通过持仓汇总去计算持仓成本和持仓盈亏规则如下：</p>
<pre><code>大商所先开先平持仓成本 = PositionCost- PositionCostOffset
</code></pre>
<p>大商所持仓盈亏：</p>
<pre><code>多头：PositionProfit = LastPrice*Position*VolumeMultiple - 
（PositionCost - PositionCostOffset）
空头：PositionProfit = （PositionCost - PositionCostOffset） - 
LastPrice*Position*VolumeMultiple 
</code></pre>
<span class="anchor" id="70a3b280-793f-4a8f-8f8d-30aab8118ed3"></span>
## 6.代码示例
<p>场景：现有c1909-P-1680和c1909-C-2020各一手的投机卖仓，申请组合代码示例如下：</p>
<pre><code>    CThostFtdcInputCombActionField a = { 0 };
    strcpy_s(a.BrokerID, “9999”);
    strcpy_s(a.InvestorID, “00001”);
    strcpy_s(a.InstrumentID, “STG c1909-P-1680&amp;c1909-C-2020”);
    strcpy_s(a.CombActionRef, "1");
    strcpy_s(a.UserID, “00001”);
    a.Direction = THOST_FTDC_D_Sell;
    a.Volume = 1;
    a.CombDirection = THOST_FTDC_CMDR_Comb;
    a.HedgeFlag = THOST_FTDC_HF_Speculation;
    strcpy_s(a.ExchangeID, “DCE”);
    m_pUserApi-&gt;ReqCombActionInsert(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="c77d7a86-11d9-4b3f-8a47-6c10961b17aa"></span>
## 7.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">查询合约的时候发现合约id不全</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>对于老版本api如果有查询组合合约，或者收到的组合合约id超过了30个字符，超过的部分会被截断，行情中也是如此。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
