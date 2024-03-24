<p>请求查询转帐银行响应，当执行ReqQryTransferBank后，该方法被调用。</p>
<span class="anchor" id="61aceb60-f3bc-4539-a8e7-0609ed42b7cb"></span>
## 1.函数原型
<p>virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5c57876f-03f0-4e01-841f-85a2e90cfad4"></span>
## 2.参数
<p>pTransferBank：转帐银行</p>
<pre><code>struct CThostFtdcTransferBankField
{
    ///银行代码
    TThostFtdcBankIDType BankID;
    ///银行分中心代码
    TThostFtdcBankBrchIDType BankBrchID;
    ///银行名称
    TThostFtdcBankNameType BankName;
    ///是否活跃
    TThostFtdcBoolType IsActive;
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
<span class="anchor" id="b4a09c5e-2e12-4795-bdf2-cb38f598f42f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="551c35ef-f1c1-4ef2-a1a6-c94d9d19e4a2"></span>
## 4.FAQ
<p>无</p>
