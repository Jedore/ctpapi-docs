<p>请求查询投资者结算结果，对应响应OnRspQrySettlementInfo。可以查询当天或历史结算单，也可以查询月结算单，但是前提是CTP柜台生成了相应的日或月结算单。</p>
<span class="anchor" id="2f7cf0e2-b022-4270-94ef-7a512c0edbfa"></span>
## 1.函数原型
<p>virtual int ReqQrySettlementInfo(CThostFtdcQrySettlementInfoField *pQrySettlementInfo, int nRequestID) = 0;</p>
<span class="anchor" id="6840e254-6b46-4506-9230-b107a9bf320d"></span>
## 2.参数
<p>pQrySettlementInfo：查询投资者结算结果</p>
<pre><code>struct CThostFtdcQrySettlementInfoField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///交易日
    TThostFtdcDateType TradingDay;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
};
</code></pre>
<p>TradingDay：查询某一天的结算单，填写格式为“yyyymmdd”；查询某一月的结算单，填写格式为“yyyymm”</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="36c9414d-d43b-4a0a-9ab0-f67e6dfa0c23"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="865ef694-6031-4d6a-b999-dcc52bf16369"></span>
## 4.调用示例
<pre><code>CThostFtdcQrySettlementInfoField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.TradingDay,“20180101”);
m_pUserApi-&gt;ReqQrySettlementInfo(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="344b72d0-7938-443c-965f-5ed3a6784ac6"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">为什么我查不到月结单？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>这有可能是CTP系统里没有生成你的月结算单。CTP的日结算单是需要每天结算的时候业务人员去点击生成的，月结算单也是需要定期生成的。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
