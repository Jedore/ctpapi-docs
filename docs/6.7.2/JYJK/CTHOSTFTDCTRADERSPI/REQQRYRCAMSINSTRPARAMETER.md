<p>请求RCAMS同合约风险对冲参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINSTRPARAMETER/">OnRspQryRCAMSInstrParameter</a></p>
<span class="anchor" id="8de2f7d8-da4f-4a7e-af52-2700844421a3"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSInstrParameter(CThostFtdcQryRCAMSInstrParameterField *pQryRCAMSInstrParameter, int nRequestID) = 0;</p>
<span class="anchor" id="3a4ebd3e-51f5-423e-8ce1-e7ba19591555"></span>
## 2.参数
<p>pQryRCAMSInstrParameter：RCAMS同合约风险对冲参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="1ed1810e-dfc5-4c96-9465-33934480443d"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b941040a-3e5c-4205-8dc5-539510fd3f0b"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="2d95ef00-1dda-48e1-bdfe-6bd1de2fb5ed"></span>
## 5.FAQ
<p>无</p>
