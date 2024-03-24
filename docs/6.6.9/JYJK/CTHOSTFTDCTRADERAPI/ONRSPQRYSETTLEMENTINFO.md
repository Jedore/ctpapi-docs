<p>请求查询投资者结算结果响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSETTLEMENTINFO/">ReqQrySettlementInfo</a>后，该方法被调用。</p>
<span class="anchor" id="aee18e80-33c7-4daf-a5ca-a71338572f6e"></span>
## 1.函数原型
<p>virtual void OnRspQrySettlementInfo(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="0ab831a7-8e6b-4de6-bc8e-30bc3b1c3db0"></span>
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
<span class="anchor" id="5352dbad-217b-48a9-b4fe-417075ce7a08"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9e546fce-d16e-4d4c-b34e-d26923335228"></span>
## 4.FAQ
<p>无</p>
