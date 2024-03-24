<p>查询保证金监管系统经纪公司资金账户密钥响应，此接口已弃用。 </p>
<span class="anchor" id="3a92c2a7-e89b-431c-8cea-8666df7a9dd8"></span>
## 1.函数原型
<p>virtual void OnRspQryCFMMCTradingAccountKey(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="052fc12b-5225-49d1-b420-116aab874340"></span>
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
<span class="anchor" id="1c057f20-99cd-4892-bc04-94c90e3beb3c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e82be282-ba43-4f9c-ab6c-b46a4aa20941"></span>
## 4.FAQ
<p>无</p>
