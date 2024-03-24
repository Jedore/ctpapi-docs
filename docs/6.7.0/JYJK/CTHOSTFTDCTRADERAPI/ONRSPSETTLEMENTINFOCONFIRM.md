<p>投资者结算结果确认响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQSETTLEMENTINFOCONFIRM/">ReqSettlementInfoConfirm</a>后，该方法被调用。</p>
<span class="anchor" id="17002b5e-adeb-40c0-b2e3-043f1462a2bc"></span>
## 1.函数原型
<p>virtual void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d615b48a-fff2-4003-a173-df77f4abd489"></span>
## 2.参数
<p>pSettlementInfoConfirm：投资者结算结果确认信息</p>
<pre><code>struct CThostFtdcSettlementInfoConfirmField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///确认日期
    TThostFtdcDateType ConfirmDate;
    ///确认时间
    TThostFtdcTimeType ConfirmTime;
    ///结算编号
    TThostFtdcSettlementIDType SettlementID;
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
<span class="anchor" id="d34b1434-e906-41eb-81b0-929e9a4e0d92"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5dd848ab-b43f-4dca-863b-d83eefd3da0e"></span>
## 4.FAQ
<p>无</p>
