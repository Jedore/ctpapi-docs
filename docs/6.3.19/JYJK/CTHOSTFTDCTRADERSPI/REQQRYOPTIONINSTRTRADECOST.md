<p>请求查询期权交易成本，该函数用于查期权保证金，对应响应OnRspQryOptionInstrTradeCost。</p>
<blockquote>
<p><code>保证金=max(权利金+FixedMargin,MiniMargin)</code>，用户可根据此公式计算实时保证金。</p>
</blockquote>
<span class="anchor" id="a4a5e9a7-c4a2-4192-897e-61a93a5782a7"></span>
## 1.函数原型
<p>virtual int ReqQryOptionInstrTradeCost(CThostFtdcQryOptionInstrTradeCostField *pQryOptionInstrTradeCost, int nRequestID) = 0;</p>
<span class="anchor" id="2da00ff7-ced9-4007-85ae-fd66a7fdb26d"></span>
## 2.参数
<p>pQryOptionInstrTradeCost：期权交易成本查询</p>
<pre><code>struct CThostFtdcQryOptionInstrTradeCostField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///期权合约报价
    TThostFtdcPriceType InputPrice;
    ///标的价格,填0则用昨结算价
    TThostFtdcPriceType UnderlyingPrice;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="dc725ea3-bd28-4b55-a6c0-3a3621639949"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d2abb7d1-7986-4800-bd58-c164270ab0a4"></span>
## 4.调用示例
<pre><code>CThostFtdcQryOptionInstrTradeCostField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
a.HedgeFlag = THOST_FTDC_HF_Speculation;
a.InputPrice = 300; 
m_pUserApi-&gt;ReqQryOptionInstrTradeCost(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="8985455b-fd4a-4244-86cf-7691052e8c98"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">为什么我用这个接口算出来的保证金跟资金查询得到的保证金占用不一致？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>ReqQryOptionInstrTradeCost计算出的期权保证金跟资金查询里的期权保证金的计算方式不一样。</p>
<p>ReqQryOptionInstrTradeCost只是估计计算，因为其使用的公式（保证金=max(权利金+FixedMargin,MiniMargin)）中的权利金部分在计算时使用的期权价格是InputPrice。</p>
<p>而资金查询里的期权保证金计算公式中的期权价格是使用max算法（max(昨结算，最新价)）得到的。</p>
<p>所以两者存在差别。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
