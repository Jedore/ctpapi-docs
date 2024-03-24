<p>请求查询投资者结算结果响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSETTLEMENTINFO/">ReqQrySettlementInfo</a>后，该方法被调用。</p>
<span class="anchor" id="1cf41e3c-0f7f-4c96-aba9-3bac8dd628f6"></span>
## 1.函数原型
<p>virtual void OnRspQrySettlementInfo(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="88017e93-587f-404a-8191-8061f6ab2256"></span>
## 2.参数
<p>pSettlementInfo：投资者结算结果</p>
<pre><code>struct CThostFtdcSettlementInfoField
{
    ///交易日
    TThostFtdcDateType TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType SettlementID;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///序号
    TThostFtdcSequenceNoType SequenceNo;
    ///消息正文
    TThostFtdcContentType Content;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="0827287c-6088-42ac-89b5-81fff415edbd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e8bc91b8-ed82-4866-9b0b-f503718a2f65"></span>
## 4.FAQ
<p>无</p>
