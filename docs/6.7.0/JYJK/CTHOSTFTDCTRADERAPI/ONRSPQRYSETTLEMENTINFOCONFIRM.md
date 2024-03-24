<p>请求查询结算信息确认响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSETTLEMENTINFOCONFIRM/">ReqQrySettlementInfoConfirm</a>后，该方法被调用。</p>
<span class="anchor" id="30ce4716-53ed-45e3-bb26-cc5fe9a9cb3c"></span>
## 1.函数原型
<p>virtual void OnRspQrySettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="57d3d2e4-4541-4815-97cf-2d70f178a86a"></span>
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
<span class="anchor" id="585b2bb2-43e0-491a-8d4a-339f1cca5ced"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0f4f9623-05c8-4085-ba0c-a1e2e76c563a"></span>
## 4.FAQ
<p>无</p>
