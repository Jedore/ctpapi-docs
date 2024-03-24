<p>申请组合录入请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQCOMBACTIONINSERT/">ReqCombActionInsert</a>后，该方法被调用</p>
<span class="anchor" id="3f3f3556-c8d8-42df-a890-f5b7c3cf1381"></span>
## 1.函数原型
<p>virtual void OnRspCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8f48f9f3-fac4-493d-9fb5-70f502ca2020"></span>
## 2.参数
<p>pInputCombAction：输入的申请组合</p>
<pre><code>struct CThostFtdcInputCombActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///组合引用
    TThostFtdcOrderRefType  CombActionRef;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///数量
    TThostFtdcVolumeType    Volume;
    ///组合指令方向
    TThostFtdcCombDirectionType CombDirection;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve2;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///前置编号
    TThostFtdcFrontIDType   FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
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
<span class="anchor" id="c332adf2-d7d5-41cd-8032-a29c325c0186"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d23d276a-d142-44c0-bc3d-6dce572bd546"></span>
## 4.FAQ
<p>无</p>
