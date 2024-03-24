<p>投资者结算结果确认，在开始每日交易前都需要先确认上一日结算单，只需要确认一次。对应响应OnRspSettlementInfoConfirm。</p>
<span class="anchor" id="a99461ab-4627-4865-aa7e-6b09ce255239"></span>
## 1.函数原型
<p>virtual int ReqSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID) = 0;</p>
<span class="anchor" id="6cfda584-9829-4341-a342-d434e81203ce"></span>
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
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="57fef739-2bd0-40e1-a1e9-d82744ae6ee8"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="cb400202-4a7d-4779-b42b-91c1b9c77afa"></span>
## 4.调用示例
<pre><code>CThostFtdcSettlementInfoConfirmField Confirm = { 0 };
strcpy_s(Confirm.BrokerID, "9999"); 
strcpy_s(Confirm.InvestorID, "1000001");
m_pUserApi-&gt;ReqSettlementInfoConfirm(&amp;Confirm, nRequestID++);
</code></pre>
<span class="anchor" id="cd679b50-57ed-4aff-a37e-deb4472a32fa"></span>
## 5.FAQ
<p>无</p>
