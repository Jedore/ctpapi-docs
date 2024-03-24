<p>请求查询合约保证金率，对应响应OnRspQryInstrumentMarginRate。如果InstrumentID填空，则返回持仓对应的合约保证金率，否则返回相应InstrumentID的保证金率。</p>
<blockquote>
<p>目前无法通过一次查询得到所有合约保证金率，如果要查询所有，则需要通过多次查询得到。</p>
</blockquote>
<span class="anchor" id="2f45658e-d3c5-4af1-8682-b5e25cc9c5b8"></span>
## 1.函数原型
<p>virtual int ReqQryInstrumentMarginRate(CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID) = 0;</p>
<span class="anchor" id="61166260-815a-4a4b-bab8-d3cdfde7e597"></span>
## 2.参数
<p>pQryInstrumentMarginRate：查询合约保证金率</p>
<pre><code>struct CThostFtdcQryInstrumentMarginRateField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="b1ec9750-0c9b-412c-9472-374f1fb0b2a1"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="471d1a22-e160-431b-b8b8-e64c8e1f85a4"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInstrumentMarginRateField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
a.HedgeFlag = THOST_FTDC_HF_Speculation;
m_pUserApi-&gt;ReqQryInstrumentMarginRate(&amp;a, 1);
</code></pre>
<span class="anchor" id="68fe40ea-46d7-4421-a92f-84f59cece250"></span>
## 5.FAQ
<p>无</p>
