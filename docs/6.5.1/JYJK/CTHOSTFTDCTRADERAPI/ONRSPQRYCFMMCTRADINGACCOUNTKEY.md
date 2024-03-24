<p>查询保证金监管系统经纪公司资金账户密钥响应，此接口已弃用。 </p>
<span class="anchor" id="0ae57400-1a03-4329-82aa-b339e6d628f7"></span>
## 1.函数原型
<p>virtual void OnRspQryCFMMCTradingAccountKey(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="f4561ea1-7740-41cf-83dc-1de4cf0a57c6"></span>
## 2.参数
<p>pCFMMCTradingAccountKey：保证金监管系统经纪公司资金账户密钥</p>
<pre><code>struct CThostFtdcCFMMCTradingAccountKeyField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///经纪公司统一编码
    TThostFtdcParticipantIDType ParticipantID;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///密钥编号
    TThostFtdcSequenceNoType KeyID;
    ///动态密钥
    TThostFtdcCFMMCKeyType CurrentKey;
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
<span class="anchor" id="1589971a-ceda-4d94-89e1-fcbd731fac99"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8cff4c67-e312-4dd7-91ed-a391d27527b0"></span>
## 4.FAQ
<p>无</p>
