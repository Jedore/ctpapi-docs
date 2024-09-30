<p>投资者结算结果确认响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQSETTLEMENTINFOCONFIRM/">ReqSettlementInfoConfirm</a>后，该方法被调用。</p>
<span class="anchor" id="789020c0-bbb8-412d-876e-86e65cef517c"></span>
## 1.函数原型
<p>virtual void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="1c442815-9885-4fc2-a394-562518839648"></span>
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
<span class="anchor" id="d6596f5e-07d2-4dd8-b574-045faeec820e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="55657563-f40d-4e7a-9708-6a3737aba00b"></span>
## 4.FAQ
<p>无</p>
