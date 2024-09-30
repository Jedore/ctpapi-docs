<p>查询保证金监管系统经纪公司资金账户密钥响应，此接口已弃用。 </p>
<span class="anchor" id="e3f27e9b-3c5f-4520-aa39-0dbc3d984ee0"></span>
## 1.函数原型
<p>virtual void OnRspQryCFMMCTradingAccountKey(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="58c353d5-af58-43be-ba0c-db6af28aae57"></span>
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
<span class="anchor" id="4c472abf-3b50-4c84-a501-5f1905ea7e6e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d71e396e-81f3-4722-b7bc-99e79dc8cd6c"></span>
## 4.FAQ
<p>无</p>
